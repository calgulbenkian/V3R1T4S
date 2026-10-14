# Run It Yourself

## 1. Verify the Shipped Object (`object/15x16x16_r2177_Q.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/15x16x16_r2177_Q.json
sha256 matches INDEX.csv (7fad12e946debb23b15ffe57e5fc3f15a8f05c1859510e5aaccb9af5907618aa)
PASS file=15x16x16_r2177_Q.json format=15x16x16 rank=2177 primes=2 log2_bound=51
rank 2177 matches INDEX.csv
== Running negative control (mutated vocab entry must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/15x16x16_r2177_Q.json`

From the V3R1T4S workspace root:

```sh
python3 runs/2026-10-14-0425/attempts/representation-absorber/code/cascade_17_18.py
```
