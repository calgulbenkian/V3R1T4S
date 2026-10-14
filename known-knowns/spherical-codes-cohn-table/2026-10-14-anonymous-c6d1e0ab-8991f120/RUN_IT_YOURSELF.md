# Run It Yourself

## 1. Verify the Shipped Object (`object/code_29_114.json`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/code_29_114.json
sha256 matches INDEX.csv (8991f120f20e9464eeb266bc9e25cad1b440ad7d53d5dbbf21527a47685b3ccf)
file=code_29_114.json PASS kind=solution_claim params=(29,114) needs_opt=False c_table=0.089759904426 c_star=0.0886557493406558116735243 gain=1.104155e-3 min_angle_deg=84.913721944786 base_ok=True(diff=1.30e-14)
== Running negative control (duplicate point must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```
