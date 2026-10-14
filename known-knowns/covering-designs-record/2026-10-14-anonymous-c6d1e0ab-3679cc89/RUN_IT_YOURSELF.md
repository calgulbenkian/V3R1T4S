# Run It Yourself

## 1. Verify the Shipped Object (`object/C_45_14_3_b58.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/C_45_14_3_b58.json
sha256 matches INDEX.csv (3679cc89320bf75dbc35662d19f4a991ec3f03fb59ee99e0afefe4eee03c95c6)
file=C_45_14_3_b58.json PASS kind=plain params=C(45,14,3) blocks=58 schonheim=45 covered=14190/14190
blocks=58 matches INDEX.csv
== Running negative control (deleting one block must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/C_45_14_3_b58.json`

Compile `how-we-built-it/covering_sa.c` with `cc -O3 -march=native -pthread -o covering_sa how-we-built-it/covering_sa.c` and run it on the `(v=45, k=14, t=3)` seed.
