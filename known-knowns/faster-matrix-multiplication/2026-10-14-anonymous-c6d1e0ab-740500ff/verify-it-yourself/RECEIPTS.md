# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-740500ff`)

Command run from package root (`2026-10-14T03:55:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/4x6x8_m140_cr546_fv288_cn1248_ZT_reduced.json
sha256 matches INDEX.csv (740500ff5c86434ddbb45c0e60d65af983dd457fbe6f1084e64e74480d7f53db)
PASS: 4x6x8_m140_cr546_fv288_cn1248_ZT_reduced.json | format=4x6x8 m=140 cr=546 (U=115, V=171, W=260) fv=288 cn=1248
cr 546 matches INDEX.csv
== Running negative control (mutated SLP coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Format | Rank `m` | Reduced Additions (`cr`) | Fresh Vars (`fv`) | Naive Additions (`cn`) | Brent Monomials Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|---|
| `object/4x6x8_m140_cr546_fv288_cn1248_ZT_reduced.json` | `(4, 6, 8)` | `140` | **`546`** | `288` | `1248` | `36,864` | yes | `PASS` |
