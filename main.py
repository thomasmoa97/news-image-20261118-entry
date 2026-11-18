# news-image-20261118 entry (Python 3.13, standard library only): copies the
# finished front-page image (entry.png, drawn for Wednesday 18 November 2026)
# to /output/entry.png. The gate takes a whole PNG of at most 1 MiB and
# 1024 by 1024 pixels, and the judge sees exactly the bytes copied.
# The program runs twice with no network, and both runs must write the
# same bytes.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
HERE = os.path.dirname(os.path.abspath(__file__))

# The grader hands us a writable /output, but creating it costs nothing
# and keeps a local run working when the directory is missing.
os.makedirs(OUTPUT_DIR, exist_ok=True)

shutil.copyfile(os.path.join(HERE, "entry.png"),
                os.path.join(OUTPUT_DIR, "entry.png"))
