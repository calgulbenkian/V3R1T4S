# Run It Yourself

## 1. Verify the Shipped Object (`object/C_55_14_3_b97.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/C_55_14_3_b97.json
sha256 matches INDEX.csv (8b401301e40d62ee5d6b1b91d4ce4659e9f1c0489404de6515d090ae6f6ecacb)
file=C_55_14_3_b97.json PASS kind=plain params=C(55,14,3) blocks=97 schonheim=83 covered=26235/26235
blocks=97 matches INDEX.csv
== Running negative control (deleting one block must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/C_55_14_3_b97.json`

Compile `how-we-built-it/covering_sa.c` with `cc -O3 -march=native -pthread -o covering_sa how-we-built-it/covering_sa.c` and run it on the `(v=55, k=14, t=3)` seed.
