# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-4a3b5594`)

Command run from package root (`2026-10-14T03:55:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/5x5x8_m144_cr612_fv279_cn1908_ZT_reduced.json
sha256 matches INDEX.csv (4a3b5594547999273c9a3e9335bc5e0ebd6e3b2a5f4971755cccf60b29b0d41f)
PASS: 5x5x8_m144_cr612_fv279_cn1908_ZT_reduced.json | format=5x5x8 m=144 cr=612 (U=148, V=178, W=286) fv=279 cn=1908
cr 612 matches INDEX.csv
== Running negative control (mutated SLP coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Format | Rank `m` | Reduced Additions (`cr`) | Fresh Vars (`fv`) | Naive Additions (`cn`) | Brent Monomials Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|---|
| `object/5x5x8_m144_cr612_fv279_cn1908_ZT_reduced.json` | `(5, 5, 8)` | `144` | **`612`** | `279` | `1908` | `40,000` | yes | `PASS` |
