# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-2e099667`)

Command run from package root (`2026-10-14T03:55:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/4x5x5_m76_cr295_fv113_cn530_ZT_reduced.json
sha256 matches INDEX.csv (2e09966726d94ad6ade2c53de92b73c0e2f78a2d39d2a4a52f50a0e61eef085d)
PASS: 4x5x5_m76_cr295_fv113_cn530_ZT_reduced.json | format=4x5x5 m=76 cr=295 (U=76, V=89, W=130) fv=113 cn=530
cr 295 matches INDEX.csv
== Running negative control (mutated SLP coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Format | Rank `m` | Reduced Additions (`cr`) | Fresh Vars (`fv`) | Naive Additions (`cn`) | Brent Monomials Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|---|
| `object/4x5x5_m76_cr295_fv113_cn530_ZT_reduced.json` | `(4, 5, 5)` | `76` | **`295`** | `113` | `530` | `10,000` | yes | `PASS` |
