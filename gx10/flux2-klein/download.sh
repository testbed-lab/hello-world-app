#!/usr/bin/env bash
# Pre-fetch FLUX.2 Klein base weights + all LoRAs listed in loras.json.
# Runs on the GX10 (or any machine with the HF cache mounted).
set -euo pipefail

MODEL="${MODEL:-black-forest-labs/FLUX.2-klein-4B}"   # Apache-2.0
CACHE="${HF_HOME:-$HOME/.cache/huggingface}"
export HF_HOME="$CACHE"

echo ">> base model: $MODEL"
hf download "$MODEL" >/dev/null || huggingface-cli download "$MODEL" >/dev/null

echo ">> LoRAs from loras.json"
python - <<'PY'
import json, subprocess, sys, shutil
cli = "hf" if shutil.which("hf") else "huggingface-cli"
with open("loras.json") as f:
    reg = json.load(f)["loras"]
for l in reg:
    print(f"  - {l['name']}  ({l['repo']})")
    r = subprocess.run([cli, "download", l["repo"]], capture_output=True, text=True)
    if r.returncode:
        print(f"    WARN: {r.stderr.splitlines()[-1] if r.stderr else 'failed'}", file=sys.stderr)
PY
echo "done. run: python app.py"
