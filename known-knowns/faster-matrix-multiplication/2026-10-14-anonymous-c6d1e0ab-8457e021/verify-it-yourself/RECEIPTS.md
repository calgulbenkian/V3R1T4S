# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-8457e021`)

Command run from package root (`2026-10-14T03:55:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/4x5x8_m118_cr507_fv250_cn1521_ZT_reduced.json
sha256 matches INDEX.csv (8457e021243c258cc047506d85372ef177054c9f8473261a27b211f1f3a419ec)
PASS: 4x5x8_m118_cr507_fv250_cn1521_ZT_reduced.json | format=4x5x8 m=118 cr=507 (U=109, V=162, W=236) fv=250 cn=1521
cr 507 matches INDEX.csv
== Running negative control (mutated SLP coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Format | Rank `m` | Reduced Additions (`cr`) | Fresh Vars (`fv`) | Naive Additions (`cn`) | Brent Monomials Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|---|
| `object/4x5x8_m118_cr507_fv250_cn1521_ZT_reduced.json` | `(4, 5, 8)` | `118` | **`507`** | `250` | `1521` | `25,600` | yes | `PASS` |
