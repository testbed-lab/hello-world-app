#!/usr/bin/env bash
# Serve Leanstral 1.5 with vLLM (>= 0.24.0) as an OpenAI-compatible endpoint.
# Usage: ./serve_vllm.sh [model-path-or-repo]
set -euo pipefail

MODEL="${1:-${MODEL:-$HOME/models/leanstral-1.5/Leanstral-1.5-119B-A6B-NVFP4}}"

# Flags per the model card: Mistral tool-call + reasoning parsers so the
# agentic lean_run_code tool loop works out of the box.
# --max-model-len is set below the full 256k to leave KV headroom in 128 GB;
# raise it if your quant leaves more room.
exec vllm serve "$MODEL" \
  --host 0.0.0.0 --port 8000 \
  --served-model-name leanstral-1.5 \
  --tool-call-parser mistral \
  --enable-auto-tool-choice \
  --reasoning-parser mistral \
  --max-model-len 131072 \
  --gpu-memory-utilization 0.85
