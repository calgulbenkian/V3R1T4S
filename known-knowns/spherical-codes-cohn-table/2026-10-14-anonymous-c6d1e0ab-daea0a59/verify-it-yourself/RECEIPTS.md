# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-daea0a59`)

Command run from package root (`2026-10-14T08:40:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/code_26_232.json
sha256 matches INDEX.csv (daea0a5983ec270c1f14df3cec70d19d99199037aba112f4e1e8b05dd4748b37)
file=code_26_232.json PASS kind=solution_claim params=(26,232) needs_opt=False c_table=0.161911811246 c_star=0.1619070097691030503945036 gain=4.801477e-6 min_angle_deg=80.682396749666 base_ok=True(diff=9.22e-13)
== Running negative control (duplicate point must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```
