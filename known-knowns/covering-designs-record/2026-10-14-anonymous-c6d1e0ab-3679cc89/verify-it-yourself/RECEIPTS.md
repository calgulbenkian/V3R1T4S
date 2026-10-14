# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-3679cc89`)

Command run from package root (`2026-10-14T08:05:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/C_45_14_3_b58.json
sha256 matches INDEX.csv (3679cc89320bf75dbc35662d19f4a991ec3f03fb59ee99e0afefe4eee03c95c6)
file=C_45_14_3_b58.json PASS kind=plain params=C(45,14,3) blocks=58 schonheim=45 covered=14190/14190
blocks=58 matches INDEX.csv
== Running negative control (deleting one block must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Cell | Blocks `b` | Standing Bar | Triples Covered | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|
| `object/C_45_14_3_b58.json` | `C(45, 14, 3)` | **`58`** | `59` | `14,190/14,190` | yes | `PASS` |
