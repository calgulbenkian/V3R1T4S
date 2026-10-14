#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python3 "$DIR/verify-it-yourself/verify_snake.py" --seeds-dir "$DIR/verify-it-yourself/seeds" --calibrate >/dev/null
OUT="$(python3 "$DIR/verify-it-yourself/verify_snake.py" --seeds-dir "$DIR/verify-it-yourself/seeds" --dim 12  "$DIR/object/sym_coil_Q12_1450.txt")"
echo "$OUT"
echo "$OUT" | grep -F "VALID COIL: n=12 used_dims=12 length=1450" >/dev/null
echo "$OUT" | grep -F "symmetric=True" >/dev/null

echo "PASS: Q_12 symmetric_coil L=1450 verified"
