# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-1d6e24c6`)

Command run from package root (`2026-10-14T03:55:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/5x5x7_m127_cr525_fv245_cn1602_ZT_reduced.json
sha256 matches INDEX.csv (1d6e24c6edebc809e6d6cfa7a3ecfec0f9b00550ebcf92c3289d510eb1f091fd)
PASS: 5x5x7_m127_cr525_fv245_cn1602_ZT_reduced.json | format=5x5x7 m=127 cr=525 (U=127, V=150, W=248) fv=245 cn=1602
cr 525 matches INDEX.csv
== Running negative control (mutated SLP coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Format | Rank `m` | Reduced Additions (`cr`) | Fresh Vars (`fv`) | Naive Additions (`cn`) | Brent Monomials Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|---|
| `object/5x5x7_m127_cr525_fv245_cn1602_ZT_reduced.json` | `(5, 5, 7)` | `127` | **`525`** | `245` | `1602` | `30,625` | yes | `PASS` |
