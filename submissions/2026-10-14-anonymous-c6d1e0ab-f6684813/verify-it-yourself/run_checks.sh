#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

python3 -c '
import json, sys
d = json.load(open("'"$DIR"'/object/deep_k1_cert.json"))
m = d["mask"]
if len(m) != 3889 or sum(m) != 58264195 or m != sorted(set(m)):
    sys.exit(1)
if str(d["x"]) != "0.9996906575658588" or int(d["B"]) != 19572 or int(d["q"]) != 30295 or int(d["k"]) != 1 or int(d["m"]) != 1 or int(d["ell"]) != 10000000000000:
    sys.exit(1)
'
OUT="$(python3 "$DIR/verify-it-yourself/verify_c3a.py" "$DIR/object/deep_k1_cert.json")"
echo "$OUT"

echo "$OUT" | grep -q '"B": 19572,'
echo "$OUT" | grep -q '"q": 30295,'
echo "$OUT" | grep -q '"k": 1,'
echo "$OUT" | grep -q '"m": 1,'
echo "$OUT" | grep -q '"ell": 10000000000000,'
echo "$OUT" | grep -q '"N_digits": 10000000000000,'
echo "$OUT" | grep -q '"mask_size": 3889,'
echo "$OUT" | grep -q '"mask_sum": 58264195,'
echo "$OUT" | grep -q '"n0": 16097580574,'
echo "$OUT" | grep -q '"nh": 0,'
echo "$OUT" | grep -q '"L": 53828044944368725,'
echo "$OUT" | grep -q '"theta_finite_lower_50d": "1.19229311147308833018077611662264204140088149782869",'
echo "$OUT" | grep -q '"beats_finite_record_by_1e7": true,'
echo "$OUT" | grep -q '"methods_agree": true,'

echo "PASS: ghr-sum-difference-c3a deep_k1_cert.json C_3a >= 1.19229311 verified"
