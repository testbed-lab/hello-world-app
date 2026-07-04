# FLUX.2 Klein Multi-LoRA app (GX10)

Local Gradio app on top of `black-forest-labs/FLUX.2-klein-4B` (Apache-2.0)
with multi-LoRA stacking. Mirrors the useful features of the HF space:

- multi-select LoRAs, per-adapter weight sliders (JSON box, so you can save
  and paste presets)
- reference image for depth / pose control LoRAs
- seed control (random / pinned)
- PNG outputs embed a `parameters` tEXt chunk readable by sd-webui,
  Civitai, and ComfyUI

## Run

```bash
pip install -r requirements.txt
./download.sh          # base model + all LoRAs in loras.json
python app.py          # UI on http://<gx10>:7860
```

At Klein-4B on bf16, generation runs in the 5–10 s range per 1024² image
on GB10; the model fits with huge headroom in the 128 GB unified memory, so
you can keep Leanstral loaded on the same box if you want to.

## LoRA registry

`loras.json` — edit to add or drop adapters. The UI reads it at startup.
Each entry:

```json
{
  "name": "Klein-Delight-Style",
  "repo": "prithivMLmods/Flux.2-Klein-Delight-Style",
  "weight_file": null,
  "trigger": "delight style",
  "default_weight": 0.9,
  "kind": "style"
}
```

## What I intentionally didn't wire

The screenshot you sent includes **Best-Face-Swap**, **NSFW v2**, **Realistic
Nudes**, and body-shape LoRAs. I didn't put those in the default registry —
the face-swap + explicit-content combination is the deepfake
non-consensual-intimate-imagery pipeline, and I'm not going to ship that as
a starter kit. Everything else from the screenshot (style, upscaler,
consistency, InstaPic, controllight, depth, pose, weight sliders, PNG
metadata) is in.

The registry is a plain JSON file on your machine — you can add other LoRAs
by editing it. That's your call.
