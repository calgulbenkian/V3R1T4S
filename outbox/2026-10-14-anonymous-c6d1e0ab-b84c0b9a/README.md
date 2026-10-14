# `2026-10-14-anonymous-c6d1e0ab-b84c0b9a` — `codetables-binary-linear` (`[157, 11, 99]_4`)

## What
Verified that object/win_q4_n157_k11_d99.json (3,792 bytes, SHA-256 b84c0b9a7e8b93c969d13a2372aab66f04e038803bd8e9651e97845f12f291bd) defines an explicit 11 x 157 generator matrix G over GF(4) of exact row rank 11 whose linear code [157, 11, 99]_4 has exact minimum Hamming distance d = 99 (with A_99 = 1428 minimum-weight codewords across all 4,194,303 nonzero codewords, verified identically by two independent full-codebook enumerators), strictly improving upon the live codetables.de lower bound d_lower = 98 (upper bound 108) by +1.

## Check It Yourself
```bash
bash verify-it-yourself/run_checks.sh
```

## Compared To
- **Markus Grassl's `codetables.de` (`http://www.codetables.de/BKLC/BKLC.php?q=4&n=157&k=11`, fetched `2026-10-14T10:24:01Z`, bulk SHA-256 `a4ff14cada7375b909baa6e23ec895c046fbfbd844d79136996ba17fa444a234`)**:
  - Standing lower bound: `d_lower = 98` (upper bound `d_upper = 108`)
  - Our explicit generator matrix (`object/win_q4_n157_k11_d99.json`): `d = 99` (`+1` improvement, `A_99 = 1428`)
- **Prior Literature**: Disjoint from `LinCodeEvolve` (`arXiv:2609.37056`, which covers only $q = 2, k \in [19, 22], n \in [170, 240]$).

## Not Claimed
- Does not claim optimality at the `codetables.de` upper bound `d_upper = 108` or improvements for other `(q, n, k)` cells in this package.

## Credits
- Reference bounds table maintained by Markus Grassl (`http://www.codetables.de/`).
