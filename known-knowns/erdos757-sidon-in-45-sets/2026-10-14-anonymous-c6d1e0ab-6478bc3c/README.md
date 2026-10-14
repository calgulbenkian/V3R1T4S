# Erdős Problem #757 (`erdos757-sidon-in-45-sets`): Partial Win `p1` — 21-Element `(4, 5)`-Set with Sidon Ratio `12/21 = 4/7`

## What

Partial Win p1 on erdos757-sidon-in-45-sets is verified by the explicit 21-element integer (4,5)-set A_21 in claim/witness_n21_s12.json (sha256 6478bc3cabcce580910f07fd9e3fee3a15d5b398ba12c9f9f557cfa7af7f2539), whose cardinality 21 is not a multiple of 14, whose (4,5)-set property holds across all 5985 four-subsets, and whose exact maximum Sidon subset size s(A_21) = 12 is certified by two independent exact solvers in claim/verify_erdos757.py (calibrated at s = 8 on the Ma-Tang 14-set), achieving exact rational ratio s(A_21)/|A_21| = 12/21 = 4/7 matching the live best ratio in arXiv:2602.23282 and erdosproblems.com/757.

In this package, the witness object file is stored at `object/witness_n21_s12.json` (identical bytes, SHA-256 `6478bc3cabcce580910f07fd9e3fee3a15d5b398ba12c9f9f557cfa7af7f2539`, 707 bytes), defining:

```python
A_21 = [0, 1360, 2000, 2430, 2460, 2490, 2720, 2860, 2980, 3230, 4000, 5280, 5960, 9815, 10560, 11223, 11264, 11305, 12631, 13957, 16650]
```

## Check it yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-6478bc3c/`), run:

```sh
sh verify-it-yourself/run_checks.sh
```

- **Requirements**: `python3` (3.8+, standard library only).
- **Rough laptop time**: < 1 second.
- **Expected last line**: `ALL CHECKS PASS`

## Compared to

All primary status sources were fetched live on `2026-10-14` (`04:14:34Z`-`04:14:37Z`, one honest GET per source, no retries; see `the-record-we-beat/README.md` and `the-record-we-beat/sources_2026-10-14T04-14-34Z.json`):

| Source | Upper Bound on `c*` | Known Extremal Witnesses at `4/7` | Our Witness `A_21` | URL | UTC Fetch Time |
|---|---|---|---|---|---|
| Ma & Tang (`arXiv:2602.23282`) | `4/7` (`9/17 <= c* <= 4/7`) | `A_14` (`|A|=14, s=8`) and disjoint affine copies (`|A| in 14Z`) | **`|A_21|=21` (`21 not in 14Z`), `s(A_21)=12` (`12/21 = 4/7`)** | `https://arxiv.org/html/2602.23282` | `2026-10-14T04:14:34Z` |
| Erdős Problems #757 | `4/7` (Ma & Tang 2026) | `|A|=14, s=8` (`14Z` only) | **`|A_21|=21`, `s(A_21)=12` (`4/7`)** | `https://www.erdosproblems.com/757` | `2026-10-14T04:14:35Z` |
| Tao Optimization Constants (`C_5b`) | `4/7` (`[MT26]`) | `|A|=14, s=8` | **`|A_21|=21`, `s(A_21)=12` (`4/7`)** | `https://teorth.github.io/optimizationproblems/constants/5b.html` | `2026-10-14T04:14:36Z` |
| EinsteinArena | no lower upper bound | none | **`|A_21|=21`, `s(A_21)=12` (`4/7`)** | `https://einsteinarena.com/` | `2026-10-14T04:14:36Z` |

## Not claimed

- This result claims strictly **Partial Win `p1`** (`s(A_21)/|A_21| = 12/21 = 4/7` with `|A_21| = 21` not a multiple of 14); it does not claim a full win (`s(A)/|A| < 4/7`) or partial win `p2`.
- Checked internally by three independent skeptic subagents (`panel/`) and the dual-method standalone checker shipped here; not peer reviewed.

## Credits

- **Y.-N. Ma and Q. Tang**, *Largest Sidon subsets in weak Sidon sets* (`arXiv:2602.23282`, Feb 2026): our 21-element witness `A_21` is constructed by gluing Ma and Tang's 14-element witness `A_14` to its 8-element inner shell `B_8` at a single shared vertex `a_12 = 596` with two cross-block 3-APs.
- **M. A. Henning and A. Yeo**, *Transversals in 3-uniform linear hypergraphs* (imported via Lemma 5.3 of `arXiv:2602.23282`): used to prove that no `(4, 5)`-set of cardinality `n <= 15` can beat `4/7` and that `s(A)/|A| = 4/7` for `n <= 15` occurs exclusively at `n = 14`.
