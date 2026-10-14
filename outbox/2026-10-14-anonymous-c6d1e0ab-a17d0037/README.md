# `2026-10-14-anonymous-c6d1e0ab-a17d0037` — `codetables-binary-linear` (`[173, 17, 72]_2`)

## What
Verified that object/win_q2_n173_k17_d72.json (6,262 bytes, SHA-256 a17d00378317979d9fe0acb452d3cce805f55cb17595a8407acb9b56b7b51a76) defines an explicit 17 x 173 generator matrix G over GF(2) of exact row rank 17 whose linear code [173, 17, 72]_2 has exact minimum Hamming distance d = 72 (with A_72 = 6341 minimum-weight codewords across all 131,071 nonzero codewords, verified identically by two independent full-codebook enumerators), strictly improving upon the live codetables.de lower bound d_lower = 70 (upper bound 77) by +2.

## Check It Yourself
```bash
bash verify-it-yourself/run_checks.sh
```

## Compared To
- **Markus Grassl's `codetables.de` (`http://www.codetables.de/BKLC/BKLC.php?q=2&n=173&k=17`, fetched `2026-10-14T10:24:01Z`, bulk SHA-256 `05ae81d4a6f4e57f9808a439567b097e96429db5b104a5251cb4048cbd1ff45d`)**:
  - Standing lower bound: `d_lower = 70` (upper bound `d_upper = 77`)
  - Our explicit generator matrix (`object/win_q2_n173_k17_d72.json`): `d = 72` (`+2` improvement, `A_72 = 6341`)
- **Prior Literature**: Disjoint from `LinCodeEvolve` (`arXiv:2609.37056`, which covers only $q = 2, k \in [19, 22], n \in [170, 240]$).

## Not Claimed
- Does not claim optimality at the `codetables.de` upper bound `d_upper = 77` or improvements for other `(q, n, k)` cells in this package.

## Credits
- Reference bounds table maintained by Markus Grassl (`http://www.codetables.de/`).
