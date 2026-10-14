#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python3 "$DIR/verify-it-yourself/verify_hsp.py" --data-dir "$DIR/verify-it-yourself/data" --calibrate >/dev/null
OUT="$(python3 "$DIR/verify-it-yourself/verify_hsp.py" --dim 4 --n 170 --data-dir "$DIR/verify-it-yourself/data" "$DIR/object/WIN_hsp4_170_polished.txt")"
echo "$OUT"
echo "$OUT" | grep -F "VALID PACKING: d=4 N=170" >/dev/null
echo "$OUT" | grep -F "r* (25 digits) = 0.2156450594683900081281903" >/dev/null
echo "$OUT" | grep -F "total_sq_norm  = 95.6294526810582612158986949" >/dev/null
echo "$OUT" | grep -F "RECORD CONFIRMED" >/dev/null
echo "PASS: hsp4 N=170 r*=0.2156450594683900081281903 verified"
