# Run It Yourself

## 1. Verify the Shipped Object (`object/4x4x7_m85_cr317_fv119_cn631_ZT_reduced.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/4x4x7_m85_cr317_fv119_cn631_ZT_reduced.json
sha256 matches INDEX.csv (ec055cb50ec26544703661a163796d145b57c732a2fa1586abb9d7dadfcb56dc)
PASS: 4x4x7_m85_cr317_fv119_cn631_ZT_reduced.json | format=4x4x7 m=85 cr=317 (U=80, V=92, W=145) fv=119 cn=631
cr 317 matches INDEX.csv
== Running negative control (mutated SLP coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/4x4x7_m85_cr317_fv119_cn631_ZT_reduced.json`

From the V3R1T4S workspace root:

```sh
cc -O3 -pthread -o runs/2026-10-14-0312/attempts/c-evaluator-optimizer/code/cse_opt runs/2026-10-14-0312/attempts/c-evaluator-optimizer/code/cse_opt.c
python3 runs/2026-10-14-0312/attempts/representation-absorber/code/flip_cse.py
```
