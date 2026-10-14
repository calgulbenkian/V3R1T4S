#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

python3 -c '
import json, sys
d = json.load(open("'"$DIR"'/object/best_k2_finite_cert.json"))
m = d["mask"]
if len(m) != 6641 or sum(m) != 110153923 or m != sorted(set(m)):
    sys.exit(1)
if str(d["x"]) != "0.9996636510501249" or int(d["B"]) != 21700 or int(d["q"]) != 25879 or int(d["k"]) != 2 or int(d["m"]) != 1 or int(d["ell"]) != 10000000000000000:
    sys.exit(1)
'
grep -q '"h_cost": 1000000000,' "$DIR/object/best_k2_finite_cert.json"
OUT="$(python3 "$DIR/verify-it-yourself/verify_c3a.py" "$DIR/object/best_k2_finite_cert.json")"
echo "$OUT"

echo "$OUT" | grep -q '"B": 21700,'
echo "$OUT" | grep -q '"q": 25879,'
echo "$OUT" | grep -q '"k": 2,'
echo "$OUT" | grep -q '"m": 1,'
echo "$OUT" | grep -q '"ell": 10000000000000000,'
echo "$OUT" | grep -q '"N_digits": 20000000000000000,'
echo "$OUT" | grep -q '"mask_size": 6641,'
echo "$OUT" | grep -q '"mask_sum": 110153923,'
echo "$OUT" | grep -q '"n0": 32819948656,'
echo "$OUT" | grep -q '"nh": 0,'
echo "$OUT" | grep -q '"L": 98800205183398657643,'
echo "$OUT" | grep -q '"theta_finite_lower_50d": "1.19298973462186362590382529754753993070825527359705",'
echo "$OUT" | grep -q '"beats_finite_record_by_1e7": true,'
echo "$OUT" | grep -q '"methods_agree": true,'

echo "PASS: ghr-sum-difference-c3a best_k2_finite_cert.json C_3a >= 1.19298973 verified"
