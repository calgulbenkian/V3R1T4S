# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-f8ea2f10`)

Command run from package root (`2026-10-14T03:55:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/4x6x7_m123_cr505_fv237_cn1573_ZT_reduced.json
sha256 matches INDEX.csv (f8ea2f1002c2100a61df1ee19be3bf1335a80c1990b2a3d4f3217feebcc52869)
PASS: 4x6x7_m123_cr505_fv237_cn1573_ZT_reduced.json | format=4x6x7 m=123 cr=505 (U=121, V=159, W=225) fv=237 cn=1573
cr 505 matches INDEX.csv
== Running negative control (mutated SLP coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Format | Rank `m` | Reduced Additions (`cr`) | Fresh Vars (`fv`) | Naive Additions (`cn`) | Brent Monomials Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|---|
| `object/4x6x7_m123_cr505_fv237_cn1573_ZT_reduced.json` | `(4, 6, 7)` | `123` | **`505`** | `237` | `1573` | `28,224` | yes | `PASS` |
