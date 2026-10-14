# Run It Yourself

## 1. Verify the Shipped Object (`object/4x4x6_m73_cr275_fv101_cn534_ZT_reduced.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/4x4x6_m73_cr275_fv101_cn534_ZT_reduced.json
sha256 matches INDEX.csv (9e2abca2c586a6020b90ae6e020dabb4b00f47dead9e4bea48a804452a8dfff7)
PASS: 4x4x6_m73_cr275_fv101_cn534_ZT_reduced.json | format=4x4x6 m=73 cr=275 (U=71, V=78, W=126) fv=101 cn=534
cr 275 matches INDEX.csv
== Running negative control (mutated SLP coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/4x4x6_m73_cr275_fv101_cn534_ZT_reduced.json`

From the V3R1T4S workspace root:

```sh
cc -O3 -pthread -o runs/2026-10-14-0312/attempts/c-evaluator-optimizer/code/cse_opt runs/2026-10-14-0312/attempts/c-evaluator-optimizer/code/cse_opt.c
python3 runs/2026-10-14-0312/attempts/representation-absorber/code/flip_cse.py
```
