# Run It Yourself

## 1. Verify the Shipped Object (`object/C_38_16_3_b25.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/C_38_16_3_b25.json
sha256 matches INDEX.csv (fd58604086de7221e9e4ccea5e65d1475e75fc6e34d0efd50edff09080eb9643)
file=C_38_16_3_b25.json PASS kind=plain params=C(38,16,3) blocks=25 schonheim=19 covered=8436/8436
blocks=25 matches INDEX.csv
== Running negative control (deleting one block must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

## 2. How to Rebuild `object/C_38_16_3_b25.json`

Compile `how-we-built-it/covering_sa.c` with `cc -O3 -march=native -pthread -o covering_sa how-we-built-it/covering_sa.c` and run it on the `(v=38, k=16, t=3)` seed.
