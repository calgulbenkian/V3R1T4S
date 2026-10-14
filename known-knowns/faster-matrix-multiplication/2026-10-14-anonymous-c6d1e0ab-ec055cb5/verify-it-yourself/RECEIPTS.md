# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-ec055cb5`)

Command run from package root (`2026-10-14T03:55:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/4x4x7_m85_cr317_fv119_cn631_ZT_reduced.json
sha256 matches INDEX.csv (ec055cb50ec26544703661a163796d145b57c732a2fa1586abb9d7dadfcb56dc)
PASS: 4x4x7_m85_cr317_fv119_cn631_ZT_reduced.json | format=4x4x7 m=85 cr=317 (U=80, V=92, W=145) fv=119 cn=631
cr 317 matches INDEX.csv
== Running negative control (mutated SLP coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Format | Rank `m` | Reduced Additions (`cr`) | Fresh Vars (`fv`) | Naive Additions (`cn`) | Brent Monomials Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|---|
| `object/4x4x7_m85_cr317_fv119_cn631_ZT_reduced.json` | `(4, 4, 7)` | `85` | **`317`** | `119` | `631` | `12,544` | yes | `PASS` |
