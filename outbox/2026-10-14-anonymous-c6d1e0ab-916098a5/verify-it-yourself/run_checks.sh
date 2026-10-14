#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python3 "$DIR/verify-it-yourself/verify_snake.py" --seeds-dir "$DIR/verify-it-yourself/seeds" --calibrate >/dev/null
OUT="$(python3 "$DIR/verify-it-yourself/verify_snake.py" --seeds-dir "$DIR/verify-it-yourself/seeds" --dim 13  "$DIR/object/sym_coil_Q13_2870.txt")"
echo "$OUT"
echo "$OUT" | grep -F "VALID COIL: n=13 used_dims=13 length=2870" >/dev/null
echo "$OUT" | grep -F "symmetric=True" >/dev/null

echo "PASS: Q_13 symmetric_coil L=2870 verified"
