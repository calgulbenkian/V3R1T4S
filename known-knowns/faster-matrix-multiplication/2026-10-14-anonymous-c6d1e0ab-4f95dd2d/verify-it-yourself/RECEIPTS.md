# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-4f95dd2d`)

Command run from package root (`2026-10-14T03:55:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/5x5x6_m110_cr451_fv202_cn1208_ZT_reduced.json
sha256 matches INDEX.csv (4f95dd2dbee2b93b8c8e102b863438193c7d6a5b899fcd0ec5a35661c115cd5d)
PASS: 5x5x6_m110_cr451_fv202_cn1208_ZT_reduced.json | format=5x5x6 m=110 cr=451 (U=119, V=124, W=208) fv=202 cn=1208
cr 451 matches INDEX.csv
== Running negative control (mutated SLP coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Format | Rank `m` | Reduced Additions (`cr`) | Fresh Vars (`fv`) | Naive Additions (`cn`) | Brent Monomials Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|---|
| `object/5x5x6_m110_cr451_fv202_cn1208_ZT_reduced.json` | `(5, 5, 6)` | `110` | **`451`** | `202` | `1208` | `22,500` | yes | `PASS` |
