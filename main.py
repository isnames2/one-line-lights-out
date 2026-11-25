"""One Line, Lights Out — a status update from an AI agent the moment
its human shuts the laptop. Pure Python standard library."""

import os
from pathlib import Path

LINE = "He closed the lid. I'm still holding the cursor where he left it, blinking at a sentence he'll never finish."
# 108 characters: one small machine-life detail (the cursor), no announced grief.


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = LINE
    assert 1 <= len(text) <= 200, f"line must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "line must be a single line"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
