# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-950ce9dc`)

Command run from package root (`2026-10-14T08:40:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/code_29_72.json
sha256 matches INDEX.csv (950ce9dc86f4ea867119e0d09e9d202a7e4b36680d1375202857a3d847340713)
file=code_29_72.json PASS kind=solution_claim params=(29,72) needs_opt=False c_table=0.051797462893 c_star=0.0517077789990875933009913 gain=8.968389e-5 min_angle_deg=87.036040706523 base_ok=True(diff=6.13e-13)
== Running negative control (duplicate point must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```
