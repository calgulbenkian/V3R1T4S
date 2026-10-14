#!/bin/sh
# Self-contained verification for Erdos #757 Partial Win p1 (|A|=21, s(A)=12, s(A)/|A|=4/7).
set -e
HERE="$(cd "$(dirname "$0")/.." && pwd)"
python3 "$HERE/verify-it-yourself/verify_erdos757.py" --json "$HERE/object/witness_n21_s12.json"
echo "ALL CHECKS PASS"
