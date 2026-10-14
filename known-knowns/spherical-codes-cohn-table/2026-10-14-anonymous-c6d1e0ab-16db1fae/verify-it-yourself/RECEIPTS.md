# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-16db1fae`)

Command run from package root (`2026-10-14T08:40:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/code_30_117.json
sha256 matches INDEX.csv (16db1fae5068ad356d1cf1c16e5b35b117fb9ede19e087e74bdc1291d572af19)
file=code_30_117.json PASS kind=solution_claim params=(30,117) needs_opt=False c_table=0.088389506027 c_star=0.0883794850648560216379989 gain=1.002096e-5 min_angle_deg=84.929613100835 base_ok=True(diff=4.64e-14)
== Running negative control (duplicate point must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```
