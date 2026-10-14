# Run It Yourself — `2026-10-14-anonymous-c6d1e0ab-3fc25411`

Run the standalone Python 3 stdlib verifier from the package root:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:

```text
{"file": "G_14_3_N1117.edges", "file_bytes": 62388, "N": 1117, "edges": 7785, "loops": 0, "duplicates": 0, "unparsable_lines": 0, "unused_labels": 0, "mindeg": 13, "maxdeg": 14, "DELTA": 14, "D": 3, "moore_bound": 2563, "live_table_entry": 1116, "live_bold_optimal": false, "trophy_case_entry": null, "baseline_to_beat": 1116, "degree_histogram": {"13": 68, "14": 1049}, "ordered_pairs_within_distance": {"0": 1117, "1": 16687, "2": 208029, "3": 1247689}, "far_pairs_at_D": 0, "far_pairs_at_D_minus_1": 1039660, "exact_diameter": 3, "negative_control_D_minus_1_rejects": true, "beats_record": true, "margin_over_baseline": 1, "valid": true}
ALL CHECKS PASS: G_14_3_N1117.edges verified (Delta=14, D=3, N=1117 > 1116)
```

You can also compile and run the standalone multi-threaded C verifier (`verify-it-yourself/ddcheck.c`):

```sh
cc -O3 -pthread -o ddcheck verify-it-yourself/ddcheck.c
./ddcheck object/G_14_3_N1117.edges 14 3 4
rm -f ddcheck
```
