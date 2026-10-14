# Run It Yourself

## 1. Verify the Shipped Object (`object/code_27_68.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/code_27_68.json
sha256 matches INDEX.csv (330c18234027e4aa5071e4c45b7893b79df1825518c984ba94c2cfe6250bba79)
file=code_27_68.json PASS kind=solution_claim params=(27,68) needs_opt=False c_table=0.051797462893 c_star=0.0517966662200721116820892 gain=7.966729e-7 min_angle_deg=87.030941010088 base_ok=True(diff=6.13e-13)
== Running negative control (duplicate point must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```
