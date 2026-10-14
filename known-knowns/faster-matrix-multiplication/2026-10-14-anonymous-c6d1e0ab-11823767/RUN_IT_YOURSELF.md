# Run It Yourself

## 1. Verify the Shipped Object (`object/5x5x5_m93_cr378_fv157_cn844_ZT_reduced.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/5x5x5_m93_cr378_fv157_cn844_ZT_reduced.json
sha256 matches INDEX.csv (118237670d742163d9f8caa3fd4e5c6a850fe9570fbb39ce3f32906b427c2a4a)
PASS: 5x5x5_m93_cr378_fv157_cn844_ZT_reduced.json | format=5x5x5 m=93 cr=378 (U=100, V=103, W=175) fv=157 cn=844
cr 378 matches INDEX.csv
== Running negative control (mutated SLP coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/5x5x5_m93_cr378_fv157_cn844_ZT_reduced.json`

From the V3R1T4S workspace root:

```sh
cc -O3 -pthread -o runs/2026-10-14-0312/attempts/c-evaluator-optimizer/code/cse_opt runs/2026-10-14-0312/attempts/c-evaluator-optimizer/code/cse_opt.c
python3 runs/2026-10-14-0312/attempts/representation-absorber/code/flip_cse.py
```
