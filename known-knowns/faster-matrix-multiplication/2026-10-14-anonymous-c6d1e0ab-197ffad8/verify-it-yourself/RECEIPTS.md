# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-197ffad8`)

Command run from package root (`2026-10-14T03:55:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/3x4x5_m47_cr159_fv60_cn277_ZT_reduced.json
sha256 matches INDEX.csv (197ffad82f4cdd3ea6899fe41fc93c1b7c16917cfa5dba26199fe8143c06292d)
PASS: 3x4x5_m47_cr159_fv60_cn277_ZT_reduced.json | format=3x4x5 m=47 cr=159 (U=39, V=46, W=74) fv=60 cn=277
cr 159 matches INDEX.csv
== Running negative control (mutated SLP coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Format | Rank `m` | Reduced Additions (`cr`) | Fresh Vars (`fv`) | Naive Additions (`cn`) | Brent Monomials Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|---|
| `object/3x4x5_m47_cr159_fv60_cn277_ZT_reduced.json` | `(3, 4, 5)` | `47` | **`159`** | `60` | `277` | `3,600` | yes | `PASS` |
