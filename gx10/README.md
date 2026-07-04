# GX10 Local AI Stack

Two workloads for the ASUS Ascent GX10 (NVIDIA GB10, 128 GB unified memory):

| Directory / file | What it is |
|---|---|
| `leanstral/` | Download, serve, smoke-test Leanstral 1.5 (Lean 4 theorem prover), plus a comparison harness against your current local model |
| `flux2-klein/` | Gradio multi-LoRA image app on FLUX.2 Klein (mirror of the HF Multi-LoRA space) |
| `HF_SHORTLIST.md` | Shortlist of open-weight models & Spaces that actually fit the GX10 — coding, agent, voice, vision, embeddings |

Both assume the stock DGX OS software stack (CUDA, Python 3.10+, `uv` or `pip`).

## Quick start

```bash
# Leanstral: download -> serve -> test
cd gx10/leanstral
./download.sh            # picks a quant that fits 128 GB
./serve_vllm.sh          # OpenAI-compatible endpoint on :8000
python smoke_test.py     # proves a small theorem end-to-end
python compare.py        # side-by-side vs your current model

# FLUX.2 Klein multi-LoRA app
cd gx10/flux2-klein
./download.sh
pip install -r requirements.txt
python app.py            # Gradio UI on :7860
```
