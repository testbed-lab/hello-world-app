"""End-to-end smoke test for a local Leanstral 1.5 endpoint.

1. Talks to the OpenAI-compatible endpoint at $LEANSTRAL_URL (default :8000).
2. Asks it to prove a trivial Lean 4 lemma.
3. If a Lean 4 REPL is on $PATH (leanprover-community/repl), compiles the
   response and reports whether it succeeds (no `sorry`, no errors).

No third-party deps — pure stdlib.
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

URL = os.environ.get("LEANSTRAL_URL", "http://localhost:8000/v1").rstrip("/")
MODEL = os.environ.get("LEANSTRAL_MODEL", "leanstral-1.5")
API_KEY = os.environ.get("LEANSTRAL_API_KEY", "not-needed")

LEMMA = (
    "Prove the following Lean 4 lemma. Reply with a single ```lean fenced "
    "code block containing the complete file, no prose.\n\n"
    "```lean\n"
    "theorem add_comm_two (a b : Nat) : a + b = b + a := by\n"
    "  sorry\n"
    "```"
)


def chat(prompt: str, *, timeout: int = 600) -> tuple[str, float]:
    body = json.dumps(
        {
            "model": MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.2,
            "max_tokens": 4096,
        }
    ).encode()
    req = urllib.request.Request(
        f"{URL}/chat/completions",
        data=body,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}",
        },
    )
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=timeout) as r:
        data = json.load(r)
    elapsed = time.time() - t0
    return data["choices"][0]["message"]["content"], elapsed


def extract_lean(text: str) -> str | None:
    m = re.search(r"```lean\s*\n(.*?)```", text, re.DOTALL)
    return m.group(1).strip() if m else None


def verify_with_lean(code: str) -> tuple[bool, str]:
    """Returns (ok, message). ok=False if `sorry` remains or errors."""
    if "sorry" in code:
        return False, "response still contains `sorry`"
    if not shutil.which("lake"):
        return False, "no `lake` on PATH — install Lean 4 + REPL to verify"
    # Best-effort: write to a scratch project and run `lake env lean`.
    # If you have leanprover-community/repl set up, this can be swapped for it.
    import tempfile
    from pathlib import Path

    with tempfile.TemporaryDirectory() as td:
        f = Path(td) / "Test.lean"
        f.write_text(code)
        try:
            out = subprocess.run(
                ["lean", str(f)],
                capture_output=True,
                text=True,
                timeout=120,
            )
        except FileNotFoundError:
            return False, "no `lean` on PATH"
        except subprocess.TimeoutExpired:
            return False, "lean check timed out"
    ok = out.returncode == 0 and not out.stderr.strip()
    return ok, (out.stderr or out.stdout).strip() or "ok"


def main() -> int:
    print(f"→ {URL}  model={MODEL}")
    try:
        answer, elapsed = chat(LEMMA)
    except Exception as e:
        print(f"FAIL: could not reach endpoint: {e}")
        return 2
    print(f"← {elapsed:.1f}s, {len(answer)} chars")
    print("---")
    print(answer)
    print("---")
    code = extract_lean(answer)
    if not code:
        print("FAIL: no ```lean``` block in response")
        return 1
    ok, msg = verify_with_lean(code)
    print(f"verify: {'PASS' if ok else 'FAIL'} — {msg}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
