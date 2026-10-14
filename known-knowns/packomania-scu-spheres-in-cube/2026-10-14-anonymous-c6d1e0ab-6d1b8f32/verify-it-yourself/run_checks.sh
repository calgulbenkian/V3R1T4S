#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$DIR/verify-it-yourself"
python3 "$DIR/verify-it-yourself/verify_scu.py" --calibrate "$DIR/verify-it-yourself/data/seeds/scu630.txt" >/dev/null
OUT="$(python3 "$DIR/verify-it-yourself/verify_scu.py" "$DIR/object/scu630.txt")"
echo "$OUT"
echo "$OUT" | grep -F "Candidate exact feasible r* (50+d):   0.06194967175853208870092462036991002" >/dev/null
echo "$OUT" | grep -F "Candidate total_sq_norm (35d):        144.39991568215544915436883960303828671" >/dev/null
echo "$OUT" | grep -F "RESULT: PASS (CONFIRMED_SOLUTION" >/dev/null
echo "PASS: scu N=630 r*=0.061949671758532088700924620370 verified"
