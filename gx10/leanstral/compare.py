"""Side-by-side compare Leanstral 1.5 vs your current brain.

Both endpoints must be OpenAI-compatible chat/completions.

Environment:
  LEANSTRAL_URL     default http://localhost:8000/v1
  LEANSTRAL_MODEL   default leanstral-1.5
  CURRENT_URL       default http://localhost:11434/v1     (Ollama)
  CURRENT_MODEL     required — the tag of your current local model
  REASONING_EFFORT  optional: low|medium|high — passed to Leanstral only

Prints a markdown table with per-prompt timings + a verification column when
a Lean 4 toolchain is available on PATH. Also drops a JSON dump next to it
for later inspection.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

PROMPTS = [
    (
        "add_comm_two",
        "Prove in Lean 4. Reply with ONE ```lean``` block, complete file, no prose.\n"
        "```lean\ntheorem add_comm_two (a b : Nat) : a + b = b + a := by\n  sorry\n```",
    ),
    (
        "mul_one",
        "Prove in Lean 4. Reply with ONE ```lean``` block, complete file, no prose.\n"
        "```lean\ntheorem mul_one_nat (n : Nat) : n * 1 = n := by\n  sorry\n```",
    ),
    (
        "list_append_nil",
        "Prove in Lean 4. Reply with ONE ```lean``` block, complete file, no prose.\n"
        "```lean\ntheorem append_nil {α : Type} (l : List α) : l ++ [] = l := by\n  sorry\n```",
    ),
    (
        "even_double",
        "Prove in Lean 4. Reply with ONE ```lean``` block, complete file, no prose.\n"
        "```lean\ntheorem two_dvd_two_mul (n : Nat) : 2 ∣ (2 * n) := by\n  sorry\n```",
    ),
    (
        "nat_pow_zero",
        "Prove in Lean 4. Reply with ONE ```lean``` block, complete file, no prose.\n"
        "```lean\ntheorem pow_zero_nat (n : Nat) : n ^ 0 = 1 := by\n  sorry\n```",
    ),
]


def chat(url: str, model: str, prompt: str, *, effort: str | None = None) -> tuple[str, float]:
    body: dict = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2,
        "max_tokens": 4096,
    }
    if effort:
        body["reasoning_effort"] = effort
    req = urllib.request.Request(
        f"{url.rstrip('/')}/chat/completions",
        data=json.dumps(body).encode(),
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer not-needed",
        },
    )
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=900) as r:
            data = json.load(r)
    except Exception as e:
        return f"[ERROR: {e}]", time.time() - t0
    elapsed = time.time() - t0
    return data["choices"][0]["message"]["content"], elapsed


def extract_lean(text: str) -> str | None:
    m = re.search(r"```lean\s*\n(.*?)```", text, re.DOTALL)
    return m.group(1).strip() if m else None


def verify(code: str | None) -> str:
    if code is None:
        return "no lean block"
    if "sorry" in code:
        return "sorry"
    if not shutil.which("lean"):
        return "no lean"
    import tempfile

    with tempfile.TemporaryDirectory() as td:
        f = Path(td) / "T.lean"
        f.write_text(code)
        try:
            out = subprocess.run(["lean", str(f)], capture_output=True, text=True, timeout=180)
        except subprocess.TimeoutExpired:
            return "timeout"
    return "ok" if out.returncode == 0 else "fail"


def main() -> int:
    leanstral_url = os.environ.get("LEANSTRAL_URL", "http://localhost:8000/v1")
    leanstral_model = os.environ.get("LEANSTRAL_MODEL", "leanstral-1.5")
    current_url = os.environ.get("CURRENT_URL", "http://localhost:11434/v1")
    current_model = os.environ.get("CURRENT_MODEL")
    effort = os.environ.get("REASONING_EFFORT")
    if not current_model:
        print("Set CURRENT_MODEL to your current brain's tag (e.g. llama3.1:70b).")
        return 2

    print(f"Leanstral: {leanstral_url}  ({leanstral_model})")
    print(f"Current : {current_url}  ({current_model})")
    print()
    results = []
    for name, prompt in PROMPTS:
        print(f"→ {name}")
        l_txt, l_t = chat(leanstral_url, leanstral_model, prompt, effort=effort)
        c_txt, c_t = chat(current_url, current_model, prompt)
        l_code, c_code = extract_lean(l_txt), extract_lean(c_txt)
        l_v, c_v = verify(l_code), verify(c_code)
        results.append(
            {
                "prompt": name,
                "leanstral": {"time_s": round(l_t, 2), "verify": l_v, "raw": l_txt},
                "current":   {"time_s": round(c_t, 2), "verify": c_v, "raw": c_txt},
            }
        )
        print(f"   leanstral {l_t:6.1f}s  {l_v}")
        print(f"   current   {c_t:6.1f}s  {c_v}")

    out = Path("compare_results.json")
    out.write_text(json.dumps(results, indent=2))
    print()
    print("| prompt | leanstral (s) | leanstral | current (s) | current |")
    print("|---|---|---|---|---|")
    for r in results:
        print(
            f"| {r['prompt']} | {r['leanstral']['time_s']} | {r['leanstral']['verify']} "
            f"| {r['current']['time_s']} | {r['current']['verify']} |"
        )
    l_ok = sum(r["leanstral"]["verify"] == "ok" for r in results)
    c_ok = sum(r["current"]["verify"] == "ok" for r in results)
    print(f"\nverified pass: leanstral {l_ok}/{len(results)}   current {c_ok}/{len(results)}")
    print(f"raw dumped to {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
