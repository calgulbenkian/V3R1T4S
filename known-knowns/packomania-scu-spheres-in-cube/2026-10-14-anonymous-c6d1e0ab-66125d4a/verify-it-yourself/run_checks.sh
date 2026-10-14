#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$DIR/verify-it-yourself"
python3 "$DIR/verify-it-yourself/verify_scu.py" --calibrate "$DIR/verify-it-yourself/data/seeds/scu467.txt" >/dev/null
OUT="$(python3 "$DIR/verify-it-yourself/verify_scu.py" "$DIR/object/scu467.txt")"
echo "$OUT"
echo "$OUT" | grep -F "Candidate exact feasible r* (50+d):   0.06789824105135698841339824029794391" >/dev/null
echo "$OUT" | grep -F "Candidate total_sq_norm (35d):        105.09606025211294794373871400098661462" >/dev/null
echo "$OUT" | grep -F "RESULT: PASS (CONFIRMED_SOLUTION" >/dev/null
echo "PASS: scu N=467 r*=0.067898241051356988413398240298 verified"
