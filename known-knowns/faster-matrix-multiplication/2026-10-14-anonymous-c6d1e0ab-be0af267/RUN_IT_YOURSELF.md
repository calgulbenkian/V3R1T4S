# Run It Yourself

## 1. Verify the Shipped Object (`object/4x6x6_m105_cr425_fv245_cn894_ZT_reduced.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/4x6x6_m105_cr425_fv245_cn894_ZT_reduced.json
sha256 matches INDEX.csv (be0af267aac940936b561873f40efc50339eebfb7005fc248a578433ced2cdc4)
PASS: 4x6x6_m105_cr425_fv245_cn894_ZT_reduced.json | format=4x6x6 m=105 cr=425 (U=108, V=131, W=186) fv=245 cn=894
cr 425 matches INDEX.csv
== Running negative control (mutated SLP coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/4x6x6_m105_cr425_fv245_cn894_ZT_reduced.json`

From the V3R1T4S workspace root:

```sh
cc -O3 -pthread -o runs/2026-10-14-0312/attempts/c-evaluator-optimizer/code/cse_opt runs/2026-10-14-0312/attempts/c-evaluator-optimizer/code/cse_opt.c
python3 runs/2026-10-14-0312/attempts/representation-absorber/code/flip_cse.py
```
