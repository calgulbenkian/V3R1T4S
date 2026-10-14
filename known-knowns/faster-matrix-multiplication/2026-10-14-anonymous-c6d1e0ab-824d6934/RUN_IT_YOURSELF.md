# Run It Yourself

## 1. Verify the Shipped Object (`object/17x17x18_r2916_Q.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/17x17x18_r2916_Q.json
sha256 matches INDEX.csv (824d69340a8b90327a8efca36e336677839b0f1048f9cfe2459a00277f922d8d)
PASS file=17x17x18_r2916_Q.json format=17x17x18 rank=2916 primes=3 log2_bound=71
rank 2916 matches INDEX.csv
== Running negative control (mutated vocab entry must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/17x17x18_r2916_Q.json`

From the V3R1T4S workspace root:

```sh
python3 runs/2026-10-14-0425/attempts/representation-absorber/code/cascade_17_18.py
```
