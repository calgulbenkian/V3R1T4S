# Run It Yourself

## 1. Verify the Shipped Object (`object/14x14x15_r1715_Q.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/14x14x15_r1715_Q.json
sha256 matches INDEX.csv (c11e45e7d7b5bd90af4d5d4f74e943bd76855bcf80599af30ffb64971485b417)
PASS file=14x14x15_r1715_Q.json format=14x14x15 rank=1715 primes=2 log2_bound=50
rank 1715 matches INDEX.csv
== Running negative control (mutated coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

You can also run the standalone verifier directly:
```sh
python3 verify-it-yourself/verify_brent.py object/14x14x15_r1715_Q.json
```

## 2. How to Rebuild `object/14x14x15_r1715_Q.json`

From the V3R1T4S workspace root:

```sh
python3 runs/2026-10-14-0004/attempts/representation-absorber/code/make_all_remaining_results.py
```
