# Verification Receipts

## 1. Exact Dual-Method Verification of `object/witness_n21_s12.json`

**Command** (run from package root):

```sh
sh verify-it-yourself/run_checks.sh
```

**Actual output**:

```text
[CALIBRATION PASS] Ma-Tang A_14: is_45=True, m=12, s1=8, s2=8, s/n=4/7
{
  "label": "witness_n21_s12.json",
  "n": 21,
  "is_45": true,
  "msg_45": "All 5985 4-subsets have >= 5 distinct differences",
  "num_3aps": 19,
  "num_4sums": 0,
  "s_method1": 12,
  "s_method2": 12,
  "s": 12,
  "ratio_str": "4/7",
  "ratio_float": 0.5714285714285714,
  "beats_4_7": false,
  "ties_4_7_non_mult_14": true,
  "witness_sidon": [
    0,
    1360,
    2000,
    2430,
    2460,
    2980,
    3230,
    5280,
    9815,
    11223,
    11264,
    13957
  ]
}
VERIFY_ERDOS757: PASS
ALL CHECKS PASS
```

## 2. Artifact Checksum

| File | Bytes | SHA-256 |
|---|---:|---|
| `object/witness_n21_s12.json` | `707` | `6478bc3cabcce580910f07fd9e3fee3a15d5b398ba12c9f9f557cfa7af7f2539` |
