# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-3fc25411`)

Command run from package root (`2026-10-14T07:42:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
{"file": "G_14_3_N1117.edges", "file_bytes": 62388, "N": 1117, "edges": 7785, "loops": 0, "duplicates": 0, "unparsable_lines": 0, "unused_labels": 0, "mindeg": 13, "maxdeg": 14, "DELTA": 14, "D": 3, "moore_bound": 2563, "live_table_entry": 1116, "live_bold_optimal": false, "trophy_case_entry": null, "baseline_to_beat": 1116, "degree_histogram": {"13": 68, "14": 1049}, "ordered_pairs_within_distance": {"0": 1117, "1": 16687, "2": 208029, "3": 1247689}, "far_pairs_at_D": 0, "far_pairs_at_D_minus_1": 1039660, "exact_diameter": 3, "negative_control_D_minus_1_rejects": true, "beats_record": true, "margin_over_baseline": 1, "valid": true}
ALL CHECKS PASS: G_14_3_N1117.edges verified (Delta=14, D=3, N=1117 > 1116)
```

| File | Cell | Vertices `N` | Edges | Standing Bar (Comellas Table) | All-Pairs BFS Pairs Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|
| `object/G_14_3_N1117.edges` | `(14, 3)` | **`1,117`** | `7,785` | `1,116` | `1,247,689` | yes | `PASS` |
