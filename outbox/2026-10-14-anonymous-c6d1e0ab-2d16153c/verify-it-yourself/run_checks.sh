#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python3 "$DIR/verify-it-yourself/verify_snake.py" --seeds-dir "$DIR/verify-it-yourself/seeds" --calibrate >/dev/null
OUT="$(python3 "$DIR/verify-it-yourself/verify_snake.py" --seeds-dir "$DIR/verify-it-yourself/seeds" --dim 12 --check-inequiv "$DIR/object/inequiv_sn12_1480.txt")"
echo "$OUT"
echo "$OUT" | grep -F "VALID SNAKE: n=12 used_dims=12 length=1480" >/dev/null
echo "$OUT" | grep -F "symmetric=False" >/dev/null
echo "$OUT" | grep -F "STRICTLY INEQUIVALENT" >/dev/null
echo "PASS: Q_12 snake L=1480 verified"
