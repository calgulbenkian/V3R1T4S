# Run It Yourself

## 1. Verify the Shipped Object (`object/2x8x8_m100_cr423_fv94_cn608_ZT_reduced.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/2x8x8_m100_cr423_fv94_cn608_ZT_reduced.json
sha256 matches INDEX.csv (1dc2a27122c50cbe852e77aab752edc1d1ec1fc2f6cb9f28a6ea47926acc1a3e)
PASS: 2x8x8_m100_cr423_fv94_cn608_ZT_reduced.json | format=2x8x8 m=100 cr=423 (U=92, V=154, W=177) fv=94 cn=608
cr 423 matches INDEX.csv
== Running negative control (mutated SLP coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/2x8x8_m100_cr423_fv94_cn608_ZT_reduced.json`

From the V3R1T4S workspace root:

```sh
cc -O3 -pthread -o runs/2026-10-14-0312/attempts/c-evaluator-optimizer/code/cse_opt runs/2026-10-14-0312/attempts/c-evaluator-optimizer/code/cse_opt.c
python3 runs/2026-10-14-0312/attempts/representation-absorber/code/flip_cse.py
```
