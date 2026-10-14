#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python3 "$DIR/verify-it-yourself/verify_hsp.py" --data-dir "$DIR/verify-it-yourself/data" --calibrate >/dev/null
OUT="$(python3 "$DIR/verify-it-yourself/verify_hsp.py" --dim 4 --n 301 --data-dir "$DIR/verify-it-yourself/data" "$DIR/object/EXT_hsp4_301.txt")"
echo "$OUT"
echo "$OUT" | grep -F "VALID PACKING: d=4 N=301" >/dev/null
echo "$OUT" | grep -F "r* (25 digits) = 0.1875249820010892044888787" >/dev/null
echo "$OUT" | grep -F "total_sq_norm  = 175.1132581185032991082293464" >/dev/null
python3 "$DIR/verify-it-yourself/verify_hsp.py" --dim 4 --n 301 --data-dir "$DIR/verify-it-yourself/data" "$DIR/verify-it-yourself/EXT_hsp4_301_baseline.txt" | grep -F "r* (25 digits) = 0.1856364718236760681178868" >/dev/null
echo "PASS: hsp4 N=301 r*=0.1875249820010892044888787 verified"
