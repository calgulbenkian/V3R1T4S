#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python3 "$DIR/verify-it-yourself/verify_snake.py" --seeds-dir "$DIR/verify-it-yourself/seeds" --calibrate >/dev/null
OUT="$(python3 "$DIR/verify-it-yourself/verify_snake.py" --seeds-dir "$DIR/verify-it-yourself/seeds" --dim 13 --check-inequiv "$DIR/object/inequiv_co13_2930.txt")"
echo "$OUT"
echo "$OUT" | grep -F "VALID COIL: n=13 used_dims=13 length=2930" >/dev/null

echo "$OUT" | grep -F "STRICTLY INEQUIVALENT" >/dev/null
echo "PASS: Q_13 coil L=2930 verified"
