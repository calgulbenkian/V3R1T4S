#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python3 "$DIR/verify-it-yourself/verify_snake.py" --seeds-dir "$DIR/verify-it-yourself/seeds" --calibrate >/dev/null
OUT="$(python3 "$DIR/verify-it-yourself/verify_snake.py" --seeds-dir "$DIR/verify-it-yourself/seeds" --dim 13 --check-inequiv "$DIR/object/inequiv_sn13_2946.txt")"
echo "$OUT"
echo "$OUT" | grep -F "VALID SNAKE: n=13 used_dims=13 length=2946" >/dev/null
echo "$OUT" | grep -F "symmetric=False" >/dev/null
echo "$OUT" | grep -F "STRICTLY INEQUIVALENT" >/dev/null
echo "PASS: Q_13 snake L=2946 verified"
