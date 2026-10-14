# Run It Yourself

## 1. Verify the Shipped Object (`object/code_28_70.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/code_28_70.json
sha256 matches INDEX.csv (cd7c56d206970b5e9b3b44ef5f31395908b4e84acf22f807c46a543556f05263)
file=code_28_70.json PASS kind=solution_claim params=(28,70) needs_opt=False c_table=0.051797462893 c_star=0.0517863124041101353861329 gain=1.115049e-5 min_angle_deg=87.031535037277 base_ok=True(diff=6.13e-13)
== Running negative control (duplicate point must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```
