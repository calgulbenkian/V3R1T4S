# Run It Yourself

## 1. Verify the Shipped Object (`object/code_30_117.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/code_30_117.json
sha256 matches INDEX.csv (16db1fae5068ad356d1cf1c16e5b35b117fb9ede19e087e74bdc1291d572af19)
file=code_30_117.json PASS kind=solution_claim params=(30,117) needs_opt=False c_table=0.088389506027 c_star=0.0883794850648560216379989 gain=1.002096e-5 min_angle_deg=84.929613100835 base_ok=True(diff=4.64e-14)
== Running negative control (duplicate point must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```
