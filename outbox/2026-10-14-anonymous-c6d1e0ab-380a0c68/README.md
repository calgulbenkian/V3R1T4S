# `2026-10-14-anonymous-c6d1e0ab-380a0c68` — `codetables-binary-linear` (`[154, 11, 97]_4`)

## What
Verified that object/win_q4_n154_k11_d97.json (3,726 bytes, SHA-256 380a0c68430f902188b249779cbd0939ac94776b49a2793a462a12895a761d3d) defines an explicit 11 x 154 generator matrix G over GF(4) of exact row rank 11 whose linear code [154, 11, 97]_4 has exact minimum Hamming distance d = 97 (with A_97 = 2448 minimum-weight codewords across all 4,194,303 nonzero codewords, verified identically by two independent full-codebook enumerators), strictly improving upon the live codetables.de lower bound d_lower = 96 (upper bound 106) by +1.

## Check It Yourself
```bash
bash verify-it-yourself/run_checks.sh
```

## Compared To
- **Markus Grassl's `codetables.de` (`http://www.codetables.de/BKLC/BKLC.php?q=4&n=154&k=11`, fetched `2026-10-14T10:24:01Z`, bulk SHA-256 `a4ff14cada7375b909baa6e23ec895c046fbfbd844d79136996ba17fa444a234`)**:
  - Standing lower bound: `d_lower = 96` (upper bound `d_upper = 106`)
  - Our explicit generator matrix (`object/win_q4_n154_k11_d97.json`): `d = 97` (`+1` improvement, `A_97 = 2448`)
- **Prior Literature**: Disjoint from `LinCodeEvolve` (`arXiv:2609.37056`, which covers only $q = 2, k \in [19, 22], n \in [170, 240]$).

## Not Claimed
- Does not claim optimality at the `codetables.de` upper bound `d_upper = 106` or improvements for other `(q, n, k)` cells in this package.

## Credits
- Reference bounds table maintained by Markus Grassl (`http://www.codetables.de/`).
