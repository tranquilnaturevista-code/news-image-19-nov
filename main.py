#!/usr/bin/env python3
"""News-image entry: copy the front-page image beside this file to the
grader's output directory as entry.png.

Standard library only, no network, deterministic: the same bytes go out
on every run. Outside the grader's container, MAKEFUN_OUTPUT_DIR stands
in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    copied = os.path.getsize(dst)
    if copied != os.path.getsize(src):
        raise SystemExit(f"copy mismatch: {src} is "
                         f"{os.path.getsize(src)} bytes, {dst} is {copied}")
    print(f"wrote {dst} ({copied} bytes)")


if __name__ == "__main__":
    main()
