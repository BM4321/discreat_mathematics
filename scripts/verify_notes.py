"""Extract every ```python block from each note, run it, and execute its test_* functions.

Usage:  python scripts/verify_notes.py ["Discrete Mathematics"]
"""
import re
import sys
import traceback
from pathlib import Path

BLOCK = re.compile(r"```python\n(.*?)```", re.DOTALL)


def verify(note: Path) -> tuple[int, list[str]]:
    code = "\n\n".join(BLOCK.findall(note.read_text(encoding="utf-8")))
    ns: dict = {"__name__": "notes_check"}
    exec(compile(code, str(note), "exec"), ns)
    failures, count = [], 0
    for name, fn in list(ns.items()):
        if name.startswith("test_") and callable(fn):
            count += 1
            try:
                fn()
            except Exception:
                failures.append(f"{note.name}::{name}\n{traceback.format_exc()}")
    return count, failures


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "Discrete Mathematics")
    total, all_failures = 0, []
    for note in sorted(root.glob("*.md")):
        try:
            count, failures = verify(note)
        except Exception:
            count, failures = 0, [f"{note.name} (block failed to run)\n{traceback.format_exc()}"]
        total += count
        all_failures += failures
        print(f"{'FAIL' if failures else 'ok  '} {note.name}: {count} tests")
    for f in all_failures:
        print("\n" + f)
    print(f"\n{total} tests, {len(all_failures)} failures")
    return 1 if all_failures else 0


if __name__ == "__main__":
    sys.exit(main())
