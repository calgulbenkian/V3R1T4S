#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$DIR/verify-it-yourself"
python3 "$DIR/verify-it-yourself/verify_scu.py" --calibrate "$DIR/verify-it-yourself/data/seeds/scu793.txt" >/dev/null
OUT="$(python3 "$DIR/verify-it-yourself/verify_scu.py" "$DIR/object/scu793.txt")"
echo "$OUT"
echo "$OUT" | grep -F "Candidate exact feasible r* (50+d):   0.05735631310193811830945618866516716" >/dev/null
echo "$OUT" | grep -F "Candidate total_sq_norm (35d):        183.72992010940995354940319621837089088" >/dev/null
echo "$OUT" | grep -F "RESULT: PASS (CONFIRMED_SOLUTION" >/dev/null
echo "PASS: scu N=793 r*=0.057356313101938118309456188665 verified"
