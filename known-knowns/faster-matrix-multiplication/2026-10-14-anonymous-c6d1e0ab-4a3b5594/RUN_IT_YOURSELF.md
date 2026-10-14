# Run It Yourself

## 1. Verify the Shipped Object (`object/5x5x8_m144_cr612_fv279_cn1908_ZT_reduced.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/5x5x8_m144_cr612_fv279_cn1908_ZT_reduced.json
sha256 matches INDEX.csv (4a3b5594547999273c9a3e9335bc5e0ebd6e3b2a5f4971755cccf60b29b0d41f)
PASS: 5x5x8_m144_cr612_fv279_cn1908_ZT_reduced.json | format=5x5x8 m=144 cr=612 (U=148, V=178, W=286) fv=279 cn=1908
cr 612 matches INDEX.csv
== Running negative control (mutated SLP coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/5x5x8_m144_cr612_fv279_cn1908_ZT_reduced.json`

From the V3R1T4S workspace root:

```sh
cc -O3 -pthread -o runs/2026-10-14-0312/attempts/c-evaluator-optimizer/code/cse_opt runs/2026-10-14-0312/attempts/c-evaluator-optimizer/code/cse_opt.c
python3 runs/2026-10-14-0312/attempts/representation-absorber/code/flip_cse.py
```
