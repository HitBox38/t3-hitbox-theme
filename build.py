#!/usr/bin/env python3
"""Build the installable Hitbox theme using only Python's standard library."""

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CSS_LIMIT = 20_000


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check that hitbox.json matches its sources without writing it.")
    args = parser.parse_args()

    theme = json.loads((ROOT / "palette.json").read_text(encoding="utf-8"))
    theme["css"] = (ROOT / "theme.css").read_text(encoding="utf-8")
    if len(theme["css"]) > CSS_LIMIT:
        parser.exit(1, f"CSS is {len(theme['css'])} characters; T3 accepts at most {CSS_LIMIT}.\n")

    output = ROOT / "hitbox.json"
    content = json.dumps(theme, indent=2).encode("utf-8")
    if args.check:
        if not output.is_file() or output.read_bytes() != content:
            parser.exit(1, "hitbox.json is out of date. Run python3 build.py.\n")
        print(f"hitbox.json is current ({len(theme['css'])} CSS characters).")
    else:
        output.write_bytes(content)
        print(f"Built hitbox.json ({len(theme['css'])} CSS characters).")


if __name__ == "__main__":
    main()
