# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-80550660`)

Command run from package root (`2026-10-14T08:40:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/code_29_145.json
sha256 matches INDEX.csv (80550660490b9e5148590d6e502ab71a9ed0067eb476238da3784ad47b23b083)
file=code_29_145.json PASS kind=solution_claim params=(29,145) needs_opt=False c_table=0.110701844288 c_star=0.1106960891058149669538693 gain=5.755182e-6 min_angle_deg=83.644556400262 base_ok=True(diff=7.58e-13)
== Running negative control (duplicate point must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```
