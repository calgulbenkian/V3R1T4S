# Run It Yourself

## 1. Verify the Shipped Object (`object/17x18x18_r2968_Q.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/17x18x18_r2968_Q.json
sha256 matches INDEX.csv (4eb5b3ba86815ff31b05fbb949342c14d177914edd72c52b2d41937bd04c63c8)
PASS file=17x18x18_r2968_Q.json format=17x18x18 rank=2968 primes=3 log2_bound=71
rank 2968 matches INDEX.csv
== Running negative control (mutated vocab entry must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/17x18x18_r2968_Q.json`

From the V3R1T4S workspace root:

```sh
python3 runs/2026-10-14-0425/attempts/representation-absorber/code/cascade_17_18.py
```
