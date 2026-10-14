#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$DIR/verify-it-yourself"
python3 "$DIR/verify-it-yourself/verify_scu.py" --calibrate "$DIR/verify-it-yourself/data/seeds/scu812.txt" >/dev/null
OUT="$(python3 "$DIR/verify-it-yourself/verify_scu.py" "$DIR/object/scu812.txt")"
echo "$OUT"
echo "$OUT" | grep -F "Candidate exact feasible r* (50+d):   0.05696282315716259072028975571734638" >/dev/null
echo "$OUT" | grep -F "Candidate total_sq_norm (35d):        189.08324279517268456877567117282260657" >/dev/null
echo "$OUT" | grep -F "RESULT: PASS (CONFIRMED_SOLUTION" >/dev/null
echo "PASS: scu N=812 r*=0.056962823157162590720289755717 verified"
