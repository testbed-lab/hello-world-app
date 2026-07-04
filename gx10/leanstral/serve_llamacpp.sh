#!/usr/bin/env bash
# Serve a Leanstral 1.5 GGUF quant with llama.cpp's OpenAI-compatible server.
# Usage: ./serve_llamacpp.sh [dir-or-gguf-file]
set -euo pipefail

TARGET="${1:-$HOME/models/leanstral-1.5}"
GGUF="$TARGET"
[ -d "$TARGET" ] && GGUF=$(find "$TARGET" -name '*Q4_K_M*.gguf' | sort | head -1)
[ -n "$GGUF" ] || { echo "No Q4_K_M gguf found under $TARGET"; exit 1; }

# -ngl 999: all layers on GPU (unified memory). --jinja enables the model's
# chat template incl. tool calls.
exec llama-server \
  -m "$GGUF" \
  --host 0.0.0.0 --port 8000 \
  --alias leanstral-1.5 \
  -ngl 999 -c 131072 --jinja
