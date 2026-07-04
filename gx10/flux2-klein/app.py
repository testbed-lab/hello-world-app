"""FLUX.2 Klein multi-LoRA Gradio app for the GX10.

Mirrors the useful features of the HF Multi-LoRA space:
  - multi-select LoRAs with per-adapter weight sliders
  - optional reference images for depth / pose control LoRAs
  - seed control (fixed / random)
  - PNG output embeds a `parameters` tEXt chunk readable by
    sd-webui / Civitai / ComfyUI

LoRA registry lives in loras.json — edit that file to add or remove
adapters; UI reads it at startup.

Run:
    pip install -r requirements.txt
    python app.py
"""

from __future__ import annotations

import io
import json
import os
import random
import time
from pathlib import Path

import gradio as gr
import torch
from PIL import Image, PngImagePlugin

try:
    from diffusers import Flux2KleinPipeline  # naming as of diffusers > 0.32
except ImportError:  # pragma: no cover
    from diffusers import DiffusionPipeline as Flux2KleinPipeline

MODEL_ID = os.environ.get("FLUX_MODEL", "black-forest-labs/FLUX.2-klein-4B")
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
DTYPE = torch.bfloat16 if DEVICE == "cuda" else torch.float32

HERE = Path(__file__).parent
REGISTRY = json.loads((HERE / "loras.json").read_text())["loras"]
BY_NAME = {l["name"]: l for l in REGISTRY}


def load_pipeline() -> Flux2KleinPipeline:
    print(f"loading {MODEL_ID} on {DEVICE} ({DTYPE})...")
    pipe = Flux2KleinPipeline.from_pretrained(MODEL_ID, torch_dtype=DTYPE)
    pipe.to(DEVICE)
    pipe.set_progress_bar_config(disable=True)
    return pipe


PIPE = load_pipeline()
ACTIVE: list[str] = []  # adapter names currently loaded on the pipe


def sync_loras(selected: list[str]) -> None:
    """Load any newly-selected LoRAs; unload dropped ones."""
    global ACTIVE
    for name in selected:
        if name in ACTIVE:
            continue
        info = BY_NAME[name]
        print(f"loading LoRA {name} ({info['repo']})")
        kwargs = {"adapter_name": name}
        if info.get("weight_file"):
            kwargs["weight_name"] = info["weight_file"]
        PIPE.load_lora_weights(info["repo"], **kwargs)
        ACTIVE.append(name)
    for name in list(ACTIVE):
        if name not in selected:
            print(f"unloading LoRA {name}")
            try:
                PIPE.delete_adapters([name])
            except Exception:
                pass
            ACTIVE.remove(name)


def build_prompt(user_prompt: str, selected: list[str]) -> str:
    triggers = [BY_NAME[n]["trigger"] for n in selected if BY_NAME[n].get("trigger")]
    return ", ".join([user_prompt, *triggers]).strip(", ")


def png_with_metadata(img: Image.Image, params_text: str) -> bytes:
    meta = PngImagePlugin.PngInfo()
    meta.add_text("parameters", params_text)
    buf = io.BytesIO()
    img.save(buf, format="PNG", pnginfo=meta)
    return buf.getvalue()


def generate(
    prompt: str,
    negative: str,
    selected: list[str],
    weights_json: str,
    ref_image: Image.Image | None,
    width: int,
    height: int,
    steps: int,
    guidance: float,
    seed: int,
    random_seed: bool,
) -> tuple[Image.Image, str, str]:
    if not prompt.strip():
        raise gr.Error("Prompt is empty.")
    sync_loras(selected)
    if selected:
        try:
            weights = json.loads(weights_json) if weights_json.strip() else {}
        except json.JSONDecodeError:
            weights = {}
        weight_values = [float(weights.get(n, BY_NAME[n]["default_weight"])) for n in selected]
        PIPE.set_adapters(selected, adapter_weights=weight_values)
    else:
        # Reset any previously-set adapters
        try:
            PIPE.set_adapters([], adapter_weights=[])
        except Exception:
            pass
        weight_values = []

    used_seed = random.randint(0, 2**31 - 1) if random_seed else int(seed)
    gen = torch.Generator(device=DEVICE).manual_seed(used_seed)

    full_prompt = build_prompt(prompt, selected)
    kwargs = dict(
        prompt=full_prompt,
        negative_prompt=negative or None,
        width=int(width),
        height=int(height),
        num_inference_steps=int(steps),
        guidance_scale=float(guidance),
        generator=gen,
    )
    # Depth / pose control LoRAs need a ref image passed via the pipeline's
    # reference input if the model supports it. Some diffusers versions expose
    # this as `image=` for img-to-img; for ControlNet-style it's `control_image`.
    if ref_image is not None and any(BY_NAME[n].get("needs_ref") for n in selected):
        kwargs["control_image"] = ref_image

    t0 = time.time()
    out = PIPE(**kwargs).images[0]
    elapsed = time.time() - t0

    lora_desc = ", ".join(f"{n}:{w:.2f}" for n, w in zip(selected, weight_values)) or "none"
    params = (
        f"{full_prompt}\n"
        f"Negative prompt: {negative}\n"
        f"Steps: {steps}, Sampler: euler, CFG scale: {guidance}, Seed: {used_seed}, "
        f"Size: {width}x{height}, Model: FLUX.2-klein, LoRAs: {lora_desc}"
    )
    out_path = HERE / "outputs" / f"gen_{used_seed}_{int(time.time())}.png"
    out_path.parent.mkdir(exist_ok=True)
    out_path.write_bytes(png_with_metadata(out, params))
    info = f"seed={used_seed}  time={elapsed:.1f}s  loras={lora_desc}\nsaved: {out_path.name}"
    return out, info, params


with gr.Blocks(title="FLUX.2 Klein Multi-LoRA (GX10)") as demo:
    gr.Markdown("# FLUX.2 Klein Multi-LoRA — local (GX10)\n"
                "PNG outputs embed `parameters` tEXt chunks (sd-webui / Civitai / ComfyUI readable).")
    with gr.Row():
        with gr.Column(scale=1):
            prompt = gr.Textbox(label="Prompt", lines=3, placeholder="a cinematic photo of ...")
            negative = gr.Textbox(label="Negative prompt", lines=2, value="")
            selected = gr.CheckboxGroup(
                choices=[l["name"] for l in REGISTRY],
                label="Active LoRAs — tick one or more",
            )
            weights_json = gr.Textbox(
                label='Weights for selected LoRAs (JSON, e.g. {"Klein-Delight-Style": 0.9})',
                value="",
                lines=2,
            )
            ref_image = gr.Image(label="Reference image (depth / pose LoRAs)", type="pil")
            with gr.Row():
                width = gr.Slider(512, 2048, 1024, step=64, label="width")
                height = gr.Slider(512, 2048, 1024, step=64, label="height")
            with gr.Row():
                steps = gr.Slider(4, 50, 28, step=1, label="steps")
                guidance = gr.Slider(0.0, 10.0, 3.5, step=0.1, label="guidance")
            with gr.Row():
                seed = gr.Number(value=0, label="seed", precision=0)
                random_seed = gr.Checkbox(value=True, label="random seed")
            btn = gr.Button("Generate", variant="primary")
        with gr.Column(scale=1):
            out_img = gr.Image(label="Result", type="pil")
            info = gr.Textbox(label="Info", lines=2)
            params_out = gr.Textbox(label="parameters (embedded in PNG)", lines=6)

    btn.click(
        generate,
        [prompt, negative, selected, weights_json, ref_image, width, height, steps, guidance, seed, random_seed],
        [out_img, info, params_out],
    )

if __name__ == "__main__":
    demo.queue().launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 7860)))
