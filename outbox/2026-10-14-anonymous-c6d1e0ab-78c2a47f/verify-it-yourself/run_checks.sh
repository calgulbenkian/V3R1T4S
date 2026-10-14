#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python3 "$DIR/verify-it-yourself/verify_snake.py" --seeds-dir "$DIR/verify-it-yourself/seeds" --calibrate >/dev/null
OUT="$(python3 "$DIR/verify-it-yourself/verify_snake.py" --seeds-dir "$DIR/verify-it-yourself/seeds" --dim 11 --check-inequiv "$DIR/object/inequiv_sn11_750.txt")"
echo "$OUT"
echo "$OUT" | grep -F "VALID SNAKE: n=11 used_dims=11 length=750" >/dev/null
echo "$OUT" | grep -F "symmetric=False" >/dev/null
echo "$OUT" | grep -F "STRICTLY INEQUIVALENT" >/dev/null
echo "PASS: Q_11 snake L=750 verified"
