# Run It Yourself

## 1. Verify the Shipped Object (`object/4x5x8_m118_cr507_fv250_cn1521_ZT_reduced.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/4x5x8_m118_cr507_fv250_cn1521_ZT_reduced.json
sha256 matches INDEX.csv (8457e021243c258cc047506d85372ef177054c9f8473261a27b211f1f3a419ec)
PASS: 4x5x8_m118_cr507_fv250_cn1521_ZT_reduced.json | format=4x5x8 m=118 cr=507 (U=109, V=162, W=236) fv=250 cn=1521
cr 507 matches INDEX.csv
== Running negative control (mutated SLP coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/4x5x8_m118_cr507_fv250_cn1521_ZT_reduced.json`

From the V3R1T4S workspace root:

```sh
cc -O3 -pthread -o runs/2026-10-14-0312/attempts/c-evaluator-optimizer/code/cse_opt runs/2026-10-14-0312/attempts/c-evaluator-optimizer/code/cse_opt.c
python3 runs/2026-10-14-0312/attempts/representation-absorber/code/flip_cse.py
```
