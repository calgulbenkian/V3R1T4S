# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-b1cc587c`)

Command run from package root (`2026-10-14T03:55:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/3x5x5_m58_cr218_fv70_cn357_ZT_reduced.json
sha256 matches INDEX.csv (b1cc587cfcd53662a62995834bb546248b177ba2dd46139fddcb726caf2d46ac)
PASS: 3x5x5_m58_cr218_fv70_cn357_ZT_reduced.json | format=3x5x5 m=58 cr=218 (U=52, V=70, W=96) fv=70 cn=357
cr 218 matches INDEX.csv
== Running negative control (mutated SLP coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Format | Rank `m` | Reduced Additions (`cr`) | Fresh Vars (`fv`) | Naive Additions (`cn`) | Brent Monomials Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|---|
| `object/3x5x5_m58_cr218_fv70_cn357_ZT_reduced.json` | `(3, 5, 5)` | `58` | **`218`** | `70` | `357` | `5,625` | yes | `PASS` |
