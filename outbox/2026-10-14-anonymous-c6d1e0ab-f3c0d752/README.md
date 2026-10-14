# `2026-10-14-anonymous-c6d1e0ab-f3c0d752` — `codetables-binary-linear` (`[158, 11, 100]_4`)

## What
Verified that object/win_q4_n158_k11_d100.json (3,815 bytes, SHA-256 f3c0d752a28835345362e0d9f4d487519ad8b113f118b07236f63efdaad788b8) defines an explicit 11 x 158 generator matrix G over GF(4) of exact row rank 11 whose linear code [158, 11, 100]_4 has exact minimum Hamming distance d = 100 (with A_100 = 2703 minimum-weight codewords across all 4,194,303 nonzero codewords, verified identically by two independent full-codebook enumerators), strictly improving upon the live codetables.de lower bound d_lower = 99 (upper bound 109) by +1.

## Check It Yourself
```bash
bash verify-it-yourself/run_checks.sh
```

## Compared To
- **Markus Grassl's `codetables.de` (`http://www.codetables.de/BKLC/BKLC.php?q=4&n=158&k=11`, fetched `2026-10-14T10:24:01Z`, bulk SHA-256 `a4ff14cada7375b909baa6e23ec895c046fbfbd844d79136996ba17fa444a234`)**:
  - Standing lower bound: `d_lower = 99` (upper bound `d_upper = 109`)
  - Our explicit generator matrix (`object/win_q4_n158_k11_d100.json`): `d = 100` (`+1` improvement, `A_100 = 2703`)
- **Prior Literature**: Disjoint from `LinCodeEvolve` (`arXiv:2609.37056`, which covers only $q = 2, k \in [19, 22], n \in [170, 240]$).

## Not Claimed
- Does not claim optimality at the `codetables.de` upper bound `d_upper = 109` or improvements for other `(q, n, k)` cells in this package.

## Credits
- Reference bounds table maintained by Markus Grassl (`http://www.codetables.de/`).
