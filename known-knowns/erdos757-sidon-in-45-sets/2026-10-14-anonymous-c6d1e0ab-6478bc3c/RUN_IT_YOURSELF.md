# Run It Yourself

## 1. Verify the Claimed 21-Element `(4, 5)`-Set (`|A_21| = 21`, `s(A_21) = 12`)

From this package's root directory:

```sh
sh verify-it-yourself/run_checks.sh
```

`verify-it-yourself/verify_erdos757.py` uses only the Python 3.8+ standard library:
1. Runs mandatory positive and negative calibration on Ma and Tang's 14-element witness `A_14` (`is_45=True, m=12, s1=8, s2=8, s/n=4/7`), `[0, 1, 2, 3]` (`is_45=False`), and `[1, 2, 3, 6]` (`is_45=True, s=3`).
2. Exhaustively checks all `binom(21, 4) = 5985` four-element subsets of `A_21` in exact integer arithmetic (`0` four-term sum collisions `a+d=b+c`, `19` three-term arithmetic progressions `a+c=2b`).
3. Certifies the exact maximum Sidon subset size `s(A_21) = 12` by two independent exact solvers: Method 1 (recursive bitmask branch-and-bound with disjoint 3-AP packing upper bound) and Method 2 (independent 0-1 ILP / DPLL minimum hitting-set solver over the conflict hypergraph).
4. Confirms `Fraction(12, 21) == Fraction(4, 7)` and `21 % 14 == 7 != 0`.

Expected output:

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

## 2. Regenerate the Family of 223 Size-21 Extremal `(4, 5)`-Sets

The algebraic block-gluing script `how-we-built-it/glue_a14_b8.py` solves the `8 x 8` linear system over `Q` gluing `A_14` to an 8-element shell `B_8` at `a_12 = 596` across all valid cross-block 3-AP pairs.
