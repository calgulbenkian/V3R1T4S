# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-90d66ebe`)

Command run from package root (`2026-10-14T03:55:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/2x4x8_m51_cr187_fv62_cn354_ZT_reduced.json
sha256 matches INDEX.csv (90d66ebee7ee850df3b63def31ba158745a7eb6c74b3a38d651aebf514bdf388)
PASS: 2x4x8_m51_cr187_fv62_cn354_ZT_reduced.json | format=2x4x8 m=51 cr=187 (U=38, V=71, W=78) fv=62 cn=354
cr 187 matches INDEX.csv
== Running negative control (mutated SLP coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Format | Rank `m` | Reduced Additions (`cr`) | Fresh Vars (`fv`) | Naive Additions (`cn`) | Brent Monomials Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|---|
| `object/2x4x8_m51_cr187_fv62_cn354_ZT_reduced.json` | `(2, 4, 8)` | `51` | **`187`** | `62` | `354` | `4,096` | yes | `PASS` |
