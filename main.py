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
    # Byte-for-byte copy: the image is the entry, so the output must be
    # identical to the source, verified by size below.
    shutil.copyfile(src, dst)
    expected = os.path.getsize(src)
    written = os.path.getsize(dst)
    if written != expected:
        raise SystemExit(f"copy mismatch: {src} is {expected} bytes, "
                         f"but {dst} is {written} bytes")
    print(f"wrote {written} bytes to {dst}")


if __name__ == "__main__":
    main()
