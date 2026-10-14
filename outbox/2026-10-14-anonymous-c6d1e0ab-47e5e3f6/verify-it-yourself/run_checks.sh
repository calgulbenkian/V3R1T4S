#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python3 "$DIR/verify-it-yourself/verify_snake.py" --seeds-dir "$DIR/verify-it-yourself/seeds" --calibrate >/dev/null
OUT="$(python3 "$DIR/verify-it-yourself/verify_snake.py" --seeds-dir "$DIR/verify-it-yourself/seeds" --dim 14  "$DIR/object/snake_Q14_5854.txt")"
echo "$OUT"
echo "$OUT" | grep -F "VALID SNAKE: n=14 used_dims=14 length=5854" >/dev/null
echo "$OUT" | grep -F "symmetric=False" >/dev/null

echo "PASS: Q_14 snake L=5854 verified"
