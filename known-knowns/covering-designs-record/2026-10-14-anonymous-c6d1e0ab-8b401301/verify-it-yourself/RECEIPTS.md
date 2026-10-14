# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-8b401301`)

Command run from package root (`2026-10-14T08:05:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/C_55_14_3_b97.json
sha256 matches INDEX.csv (8b401301e40d62ee5d6b1b91d4ce4659e9f1c0489404de6515d090ae6f6ecacb)
file=C_55_14_3_b97.json PASS kind=plain params=C(55,14,3) blocks=97 schonheim=83 covered=26235/26235
blocks=97 matches INDEX.csv
== Running negative control (deleting one block must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Cell | Blocks `b` | Standing Bar | Triples Covered | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|
| `object/C_55_14_3_b97.json` | `C(55, 14, 3)` | **`97`** | `99` | `26,235/26,235` | yes | `PASS` |
