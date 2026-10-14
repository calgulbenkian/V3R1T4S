# `2026-10-14-anonymous-c6d1e0ab-dbda9f8c` — `codetables-binary-linear` (`[172, 17, 71]_2`)

## What
Verified that object/win_q2_n172_k17_d71.json (6,228 bytes, SHA-256 dbda9f8c500349cb70c2d6c4ddbfdb3ef06e32996fd78a5b6556c2c46503438b) defines an explicit 17 x 172 generator matrix G over GF(2) of exact row rank 17 whose linear code [172, 17, 71]_2 has exact minimum Hamming distance d = 71 (with A_71 = 1751 minimum-weight codewords across all 131,071 nonzero codewords, verified identically by two independent full-codebook enumerators), strictly improving upon the live codetables.de lower bound d_lower = 70 (upper bound 76) by +1.

## Check It Yourself
```bash
bash verify-it-yourself/run_checks.sh
```

## Compared To
- **Markus Grassl's `codetables.de` (`http://www.codetables.de/BKLC/BKLC.php?q=2&n=172&k=17`, fetched `2026-10-14T10:24:01Z`, bulk SHA-256 `05ae81d4a6f4e57f9808a439567b097e96429db5b104a5251cb4048cbd1ff45d`)**:
  - Standing lower bound: `d_lower = 70` (upper bound `d_upper = 76`)
  - Our explicit generator matrix (`object/win_q2_n172_k17_d71.json`): `d = 71` (`+1` improvement, `A_71 = 1751`)
- **Prior Literature**: Disjoint from `LinCodeEvolve` (`arXiv:2609.37056`, which covers only $q = 2, k \in [19, 22], n \in [170, 240]$).

## Not Claimed
- Does not claim optimality at the `codetables.de` upper bound `d_upper = 76` or improvements for other `(q, n, k)` cells in this package.

## Credits
- Reference bounds table maintained by Markus Grassl (`http://www.codetables.de/`).
