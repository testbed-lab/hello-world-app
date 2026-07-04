#!/usr/bin/env bash
# Fetch the HF_SHORTLIST models onto the GX10. Run this ON the GX10.
#
#   ./download_shortlist.sh              # everything
#   ./download_shortlist.sh coding voice # only those groups
#
# Groups: coding agent voice vision embeddings ocr
# Requires: `hf` (pip install -U huggingface_hub) and disk space (~250 GB
# for the full set). Skips repos already fully cached.
set -euo pipefail

CACHE="${HF_HOME:-$HOME/.cache/huggingface}"
export HF_HOME="$CACHE"
CLI=$(command -v hf || command -v huggingface-cli || true)
[ -n "$CLI" ] || { echo "install huggingface_hub: pip install -U huggingface_hub"; exit 1; }

declare -A GROUPS=(
  [coding]="Qwen/Qwen3-Coder-30B-A3B-Instruct openai/gpt-oss-120b dphn/Dolphin3.0-Llama3.1-8B"
  [agent]="Salesforce/Llama-xLAM-2-70b-fc-r"
  [voice]="openai/whisper-large-v3-turbo nvidia/parakeet-tdt-0.6b-v3 hexgrad/Kokoro-82M sesame/csm-1b"
  [vision]="Qwen/Qwen3-VL-30B-A3B-Instruct openbmb/MiniCPM-V-4_5"
  [embeddings]="Qwen/Qwen3-Embedding-8B Qwen/Qwen3-Reranker-8B BAAI/bge-m3 BAAI/bge-reranker-v2-m3"
  [ocr]="stepfun-ai/GOT-OCR-2.0-hf"
)

WANT=("$@"); [ ${#WANT[@]} -eq 0 ] && WANT=(coding agent voice vision embeddings ocr)

for g in "${WANT[@]}"; do
  [ -n "${GROUPS[$g]:-}" ] || { echo "unknown group: $g"; continue; }
  echo "=== $g ==="
  for repo in ${GROUPS[$g]}; do
    echo ">> $repo"
    "$CLI" download "$repo" || echo "   WARN: $repo failed (check repo name / access)"
  done
done
echo "done. weights under $CACHE"
