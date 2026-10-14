#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python3 "$DIR/verify-it-yourself/verify_snake.py" --seeds-dir "$DIR/verify-it-yourself/seeds" --calibrate >/dev/null
OUT="$(python3 "$DIR/verify-it-yourself/verify_snake.py" --seeds-dir "$DIR/verify-it-yourself/seeds" --dim 12 --check-inequiv "$DIR/object/inequiv_co12_1468.txt")"
echo "$OUT"
echo "$OUT" | grep -F "VALID COIL: n=12 used_dims=12 length=1468" >/dev/null

echo "$OUT" | grep -F "STRICTLY INEQUIVALENT" >/dev/null
echo "PASS: Q_12 coil L=1468 verified"
