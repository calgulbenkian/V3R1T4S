# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-2ffcd289`)

Command run from package root (`2026-10-14T08:40:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/code_30_74.json
sha256 matches INDEX.csv (2ffcd2896808bedffa1ba211a4ee8dbe30cd0e3c457da8df5d09ec3745596686)
file=code_30_74.json PASS kind=solution_claim params=(30,74) needs_opt=False c_table=0.051797462893 c_star=0.0515109900801632382072426 gain=2.864728e-4 min_angle_deg=87.047330926989 base_ok=True(diff=6.13e-13)
== Running negative control (duplicate point must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```
