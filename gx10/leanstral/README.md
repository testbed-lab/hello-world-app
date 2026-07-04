# Leanstral 1.5 on the GX10

Leanstral 1.5 (`mistralai/Leanstral-1.5-119B-A6B`) is a 119B-total / 6B-active
MoE for Lean 4 theorem proving, Apache-2.0, 256k context.

## Memory math (128 GB unified)

| Precision | Weights | Fits? |
|---|---|---|
| BF16 | ~238 GB | no |
| FP8 | ~119 GB | too tight once OS + KV cache are counted |
| 4-bit (NVFP4 / AWQ / GGUF Q4_K_M) | ~65–75 GB | yes, with room for large context |

**You need a 4-bit build.** `download.sh` tries, in order:
1. An official quantized repo from Mistral (check — the release is days old)
2. A community GGUF (unsloth/bartowski usually publish within a week) for llama.cpp
3. Full BF16 weights + local AWQ quantization as last resort (slow, needs disk)

## Serving

- `serve_vllm.sh` — vLLM >= 0.24.0 with the Mistral tool-call and reasoning
  parsers, OpenAI-compatible on port 8000. Preferred if you have a
  vLLM-loadable quant (NVFP4/AWQ/FP8).
- `serve_llamacpp.sh` — llama.cpp server for a GGUF quant. Same OpenAI API
  surface, port 8000.

## Testing

- `smoke_test.py` — checks the endpoint is up, asks for a complete Lean 4
  proof of a simple lemma, prints it. If you have a Lean 4 toolchain +
  [leanprover-community/repl](https://github.com/leanprover-community/repl)
  installed, it also compiles the proof to verify it's not a `sorry`.
- `compare.py` — runs the same prompt set against Leanstral and your current
  model (any OpenAI-compatible endpoint, e.g. Ollama at
  `http://localhost:11434/v1`) and prints answers + latency side by side.

```bash
export LEANSTRAL_URL=http://localhost:8000/v1
export CURRENT_URL=http://localhost:11434/v1
export CURRENT_MODEL=<your current model name>
python compare.py
```

## Agent use (the real workflow)

For interactive proving, point [lean-lsp-mcp](https://github.com/oOo0oOo/lean-lsp-mcp)
or Mistral's `vibe --agent lean` at the local endpoint — the model is trained
to loop: emit Lean code via tool calls, read compiler errors, revise.
Set `reasoning_effort: high` for hard problems; budget millions of tokens —
its solve rate keeps climbing with test-time compute.
