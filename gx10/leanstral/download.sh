#!/usr/bin/env bash
# Download a Leanstral 1.5 build that fits the GX10's 128 GB unified memory.
set -euo pipefail

DEST="${DEST:-$HOME/models/leanstral-1.5}"
mkdir -p "$DEST"

have_repo() { hf repo info "$1" >/dev/null 2>&1 || huggingface-cli repo info "$1" >/dev/null 2>&1; }
dl() {
  echo ">> downloading $1"
  hf download "$1" --local-dir "$DEST/$(basename "$1")" "${@:2}" \
    || huggingface-cli download "$1" --local-dir "$DEST/$(basename "$1")" "${@:2}"
}

# 1) Official quantized builds (check these first — names follow Mistral's
#    usual pattern; the release is new so they may appear after this script
#    was written).
for repo in \
  mistralai/Leanstral-1.5-119B-A6B-NVFP4 \
  mistralai/Leanstral-1.5-119B-A6B-FP8 \
  mistralai/Leanstral-1.5-119B-A6B-AWQ; do
  if have_repo "$repo"; then dl "$repo"; echo "Serve with: ./serve_vllm.sh $DEST/$(basename "$repo")"; exit 0; fi
done

# 2) Community GGUF for llama.cpp (Q4_K_M ~ 70 GB). Adjust the repo name to
#    whatever quant actually gets published — search HF for "Leanstral GGUF".
for repo in \
  unsloth/Leanstral-1.5-119B-A6B-GGUF \
  bartowski/mistralai_Leanstral-1.5-119B-A6B-GGUF; do
  if have_repo "$repo"; then
    dl "$repo" --include "*Q4_K_M*"
    echo "Serve with: ./serve_llamacpp.sh $DEST/$(basename "$repo")"
    exit 0
  fi
done

# 3) Last resort: full BF16 (~240 GB disk) for local quantization.
echo "No quantized build found yet. Options:"
echo "  a) wait a few days and re-run (quants land fast after big releases)"
echo "  b) download BF16 and quantize locally:"
echo "     hf download mistralai/Leanstral-1.5-119B-A6B --local-dir $DEST/bf16"
echo "     then AWQ-quantize with llm-compressor, or convert to GGUF via llama.cpp"
exit 1
