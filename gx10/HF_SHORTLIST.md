# HF shortlist for the GX10

Open-weight models and Spaces that actually fit on your ASUS Ascent GX10
(NVIDIA GB10, 128 GB unified LPDDR5x, ~273 GB/s memory bandwidth). The
bandwidth number is the important one: MoE models with few active
parameters run **much** faster than dense models of the same total size.
Anything that doesn't fit at Q4 with KV-cache headroom is excluded.

Everything here pairs cleanly with the Leanstral (proof) and FLUX.2 Klein
(image) workloads you already have running.

## 1. General reasoning / coding

- **Qwen3-Coder-30B-A3B-Instruct** — [HF](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct)
  MoE, 3B active, ~18 GB at Q4_K_M. Best "always-on" coding daily driver
  on this box — MoE + few active params means ~100 tok/s. Non-Lean
  counterpart to Leanstral.
- **openai/gpt-oss-120b** — [HF](https://huggingface.co/openai/gpt-oss-120b)
  117B / 5.1B active, ships natively MXFP4 at ~63 GB. Near-o4-mini
  reasoning, strong tool calls, Apache-2.0. Sweet-spot single-model
  reasoner for the GX10.
- **GLM-4.6 (Unsloth dynamic Q2)** — [HF](https://huggingface.co/unsloth/GLM-4.6-GGUF)
  355B / ~32B active. UD-Q2_K_XL is ~135 GB — a stretch but drivable with
  MoE offloading; currently the highest open-weight agentic-coding score.
  Reach for it when you want a frontier reasoner, not a fast one.
- **Dolphin3.0-Llama3.1-8B** — [HF](https://huggingface.co/dphn/Dolphin3.0-Llama3.1-8B)
  (~5 GB Q4) is the no-refusal utility knife.
- **Qwen3.6-27B Heretic Uncensored** — [HF](https://huggingface.co/DavidAU/Qwen3.6-27B-Heretic-Uncensored-FINETUNE-NEO-CODE-Di-IMatrix-MAX-GGUF)
  (~16 GB Q4) — the "actually smart uncensored" option when Dolphin is
  too small.

## 2. Agent / tool-use / MCP

- **Salesforce/Llama-xLAM-2-70b-fc-r** — [HF](https://huggingface.co/Salesforce/Llama-xLAM-2-70b-fc-r)
  ~40 GB at Q4. Trained specifically on tool-use trajectories; τ-bench
  56.2%, beats GPT-4o on multi-turn agent loops. Best planner to wire to
  MCP servers. (gpt-oss-120b above is the strongest single-shot tool
  caller.)

## 3. Voice — ASR + TTS

- **openai/whisper-large-v3-turbo** — [HF](https://huggingface.co/openai/whisper-large-v3-turbo)
  ~1.6 GB, multilingual, still the best-value general ASR. Keep resident.
- **nvidia/parakeet-tdt-0.6b-v3** — [HF](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3)
  English-only but RTFx >2000 — for real-time streaming (dictation, live
  meeting transcripts).
- **hexgrad/Kokoro-82M** — [HF](https://huggingface.co/hexgrad/Kokoro-82M)
  Apache-2.0, StyleTTS2-based, 82M — #1 on TTS Arena in early 2026.
  Default TTS.
- **sesame/csm-1b** — [HF](https://huggingface.co/sesame/csm-1b)
  1B conversational, 4.7 MOS. Use when you want expressive dialogue /
  multi-speaker.

## 4. Vision (multimodal)

- **Qwen/Qwen3-VL-30B-A3B-Instruct** — [HF](https://huggingface.co/Qwen/Qwen3-VL-30B-A3B-Instruct)
  MoE, ~23 GB Q4. Best VL fit for GX10: fast, agent-capable, strong on
  screenshots and UI. Natural "see" partner to FLUX.2 Klein's "generate".
- **openbmb/MiniCPM-V-4_5** — [HF](https://huggingface.co/openbmb/MiniCPM-V-4_5)
  ~5 GB, 8B. Cheap document/OCR utility to keep resident alongside the
  bigger VL for router/classifier work.

## 5. Embeddings + rerankers (local RAG)

- **Qwen/Qwen3-Embedding-8B + Qwen/Qwen3-Reranker-8B** — [emb](https://huggingface.co/Qwen/Qwen3-Embedding-8B) · [rer](https://huggingface.co/Qwen/Qwen3-Reranker-8B)
  #1 on MTEB multilingual (70.58), 32K context, ~5 GB each at Q4.
  Top-shelf local RAG stack.
- **BAAI/bge-m3 + BAAI/bge-reranker-v2-m3** — [emb](https://huggingface.co/BAAI/bge-m3) · [rer](https://huggingface.co/BAAI/bge-reranker-v2-m3)
  MIT, 100+ languages, dense+sparse+multi-vec in one model. Lighter
  fallback when you don't need Qwen's SOTA numbers.

## 6. Useful Spaces to run locally

- **stepfun-ai/GOT-OCR-2.0-hf** — [HF](https://huggingface.co/stepfun-ai/GOT-OCR-2.0-hf)
  580M end-to-end OCR — plain text, tables, formulas, sheet music. Clone
  the Gradio app as your PDF/receipt pipeline.
- **not-lain/background-removal (RMBG-2.0)** — [Space](https://huggingface.co/spaces/not-lain/background-removal)
  Fast local BG removal — pairs directly with FLUX.2 Klein output for
  compositing.

## Skipped (don't fit or don't earn the room)

- **Qwen3-Coder-480B, DeepSeek-V4** — too big even at Q4.
- **Kimi K2** — needs 2-bit and pushes past headroom given KV-cache.
- **Qwen3-VL-235B-A22B-FP8** — ~120 GB fits weights but leaves no room
  for KV cache; use the 30B-A3B instead.
