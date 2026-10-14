#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$DIR/verify-it-yourself"
python3 "$DIR/verify-it-yourself/verify_scu.py" --calibrate "$DIR/verify-it-yourself/data/seeds/scu471.txt" >/dev/null
OUT="$(python3 "$DIR/verify-it-yourself/verify_scu.py" "$DIR/object/scu471.txt")"
echo "$OUT"
echo "$OUT" | grep -F "Candidate exact feasible r* (50+d):   0.06789824104289791070680514311122914" >/dev/null
echo "$OUT" | grep -F "Candidate total_sq_norm (35d):        106.39607068213042641161339592060476993" >/dev/null
echo "$OUT" | grep -F "RESULT: PASS (CONFIRMED_SOLUTION" >/dev/null
echo "PASS: scu N=471 r*=0.067898241042897910706805143111 verified"
