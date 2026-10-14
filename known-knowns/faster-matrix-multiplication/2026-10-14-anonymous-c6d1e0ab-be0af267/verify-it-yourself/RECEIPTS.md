# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-be0af267`)

Command run from package root (`2026-10-14T03:55:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/4x6x6_m105_cr425_fv245_cn894_ZT_reduced.json
sha256 matches INDEX.csv (be0af267aac940936b561873f40efc50339eebfb7005fc248a578433ced2cdc4)
PASS: 4x6x6_m105_cr425_fv245_cn894_ZT_reduced.json | format=4x6x6 m=105 cr=425 (U=108, V=131, W=186) fv=245 cn=894
cr 425 matches INDEX.csv
== Running negative control (mutated SLP coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Format | Rank `m` | Reduced Additions (`cr`) | Fresh Vars (`fv`) | Naive Additions (`cn`) | Brent Monomials Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|---|
| `object/4x6x6_m105_cr425_fv245_cn894_ZT_reduced.json` | `(4, 6, 6)` | `105` | **`425`** | `245` | `894` | `20,736` | yes | `PASS` |
