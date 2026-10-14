# Run It Yourself

## 1. Verify the Shipped Object (`object/13x13x14_r1499_Q.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/13x13x14_r1499_Q.json
sha256 matches INDEX.csv (d6ed9de8a92340b0c420c42344c915b8232853aef5ecee342fef7fa0c558a5f3)
PASS file=13x13x14_r1499_Q.json format=13x13x14 rank=1499 primes=2 log2_bound=50
rank 1499 matches INDEX.csv
== Running negative control (mutated coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

You can also run the standalone verifier directly:
```sh
python3 verify-it-yourself/verify_brent.py object/13x13x14_r1499_Q.json
```

## 2. How to Rebuild `object/13x13x14_r1499_Q.json`

From the V3R1T4S workspace root:

```sh
python3 runs/2026-10-14-0004/attempts/representation-absorber/code/make_all_remaining_results.py
```
