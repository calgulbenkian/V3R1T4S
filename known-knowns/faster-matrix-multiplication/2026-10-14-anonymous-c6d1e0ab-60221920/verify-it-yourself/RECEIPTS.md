# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-60221920`)

Command run from package root (`2026-10-14T03:55:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/4x5x6_m90_cr374_fv179_cn1008_ZT_reduced.json
sha256 matches INDEX.csv (60221920dc02e9a5198d6df81dbafa70f481f0367db9600fe418b21dc220584a)
PASS: 4x5x6_m90_cr374_fv179_cn1008_ZT_reduced.json | format=4x5x6 m=90 cr=374 (U=86, V=114, W=174) fv=179 cn=1008
cr 374 matches INDEX.csv
== Running negative control (mutated SLP coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Format | Rank `m` | Reduced Additions (`cr`) | Fresh Vars (`fv`) | Naive Additions (`cn`) | Brent Monomials Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|---|
| `object/4x5x6_m90_cr374_fv179_cn1008_ZT_reduced.json` | `(4, 5, 6)` | `90` | **`374`** | `179` | `1008` | `14,400` | yes | `PASS` |
