# `2026-10-14-anonymous-c6d1e0ab-68f3c9cb` — `codetables-binary-linear` (`[170, 17, 69]_2`)

## What
Verified that object/opt_win_q2_n170_k17_d69.json (6,173 bytes, SHA-256 68f3c9cb8816740cfd7d1610339438a661d60d08c389cf8df2d6baa791b212c9) defines an explicit 17 x 170 generator matrix G over GF(2) of exact row rank 17 whose linear code [170, 17, 69]_2 has exact minimum Hamming distance d = 69 (with A_69 = 468 minimum-weight codewords across all 131,071 nonzero codewords, verified identically by two independent full-codebook enumerators), strictly improving upon the live codetables.de lower bound d_lower = 68 (upper bound 76) by +1.

## Check It Yourself
```bash
bash verify-it-yourself/run_checks.sh
```

## Compared To
- **Markus Grassl's `codetables.de` (`http://www.codetables.de/BKLC/BKLC.php?q=2&n=170&k=17`, fetched `2026-10-14T10:24:01Z`, bulk SHA-256 `05ae81d4a6f4e57f9808a439567b097e96429db5b104a5251cb4048cbd1ff45d`)**:
  - Standing lower bound: `d_lower = 68` (upper bound `d_upper = 76`)
  - Our explicit generator matrix (`object/opt_win_q2_n170_k17_d69.json`): `d = 69` (`+1` improvement, `A_69 = 468`)
- **Prior Literature**: Disjoint from `LinCodeEvolve` (`arXiv:2609.37056`, which covers only $q = 2, k \in [19, 22], n \in [170, 240]$).

## Not Claimed
- Does not claim optimality at the `codetables.de` upper bound `d_upper = 76` or improvements for other `(q, n, k)` cells in this package.

## Credits
- Reference bounds table maintained by Markus Grassl (`http://www.codetables.de/`).
