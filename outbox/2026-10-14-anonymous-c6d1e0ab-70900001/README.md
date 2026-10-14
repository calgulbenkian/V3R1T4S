# `2026-10-14-anonymous-c6d1e0ab-70900001` — `codetables-binary-linear` (`[162, 11, 103]_4`)

## What
Verified that object/win_q4_n162_k11_d103.json (3,904 bytes, SHA-256 70900001eaf3d83a0097232cb01947e218e7d3c9a24955e1a6c452f83c70c88b) defines an explicit 11 x 162 generator matrix G over GF(4) of exact row rank 11 whose linear code [162, 11, 103]_4 has exact minimum Hamming distance d = 103 (with A_103 = 2907 minimum-weight codewords across all 4,194,303 nonzero codewords, verified identically by two independent full-codebook enumerators), strictly improving upon the live codetables.de lower bound d_lower = 102 (upper bound 112) by +1.

## Check It Yourself
```bash
bash verify-it-yourself/run_checks.sh
```

## Compared To
- **Markus Grassl's `codetables.de` (`http://www.codetables.de/BKLC/BKLC.php?q=4&n=162&k=11`, fetched `2026-10-14T10:24:01Z`, bulk SHA-256 `a4ff14cada7375b909baa6e23ec895c046fbfbd844d79136996ba17fa444a234`)**:
  - Standing lower bound: `d_lower = 102` (upper bound `d_upper = 112`)
  - Our explicit generator matrix (`object/win_q4_n162_k11_d103.json`): `d = 103` (`+1` improvement, `A_103 = 2907`)
- **Prior Literature**: Disjoint from `LinCodeEvolve` (`arXiv:2609.37056`, which covers only $q = 2, k \in [19, 22], n \in [170, 240]$).

## Not Claimed
- Does not claim optimality at the `codetables.de` upper bound `d_upper = 112` or improvements for other `(q, n, k)` cells in this package.

## Credits
- Reference bounds table maintained by Markus Grassl (`http://www.codetables.de/`).
