# Run It Yourself

## 1. Verify the Shipped Object (`object/2x4x8_m51_cr187_fv62_cn354_ZT_reduced.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/2x4x8_m51_cr187_fv62_cn354_ZT_reduced.json
sha256 matches INDEX.csv (90d66ebee7ee850df3b63def31ba158745a7eb6c74b3a38d651aebf514bdf388)
PASS: 2x4x8_m51_cr187_fv62_cn354_ZT_reduced.json | format=2x4x8 m=51 cr=187 (U=38, V=71, W=78) fv=62 cn=354
cr 187 matches INDEX.csv
== Running negative control (mutated SLP coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/2x4x8_m51_cr187_fv62_cn354_ZT_reduced.json`

From the V3R1T4S workspace root:

```sh
cc -O3 -pthread -o runs/2026-10-14-0312/attempts/c-evaluator-optimizer/code/cse_opt runs/2026-10-14-0312/attempts/c-evaluator-optimizer/code/cse_opt.c
python3 runs/2026-10-14-0312/attempts/representation-absorber/code/flip_cse.py
```
