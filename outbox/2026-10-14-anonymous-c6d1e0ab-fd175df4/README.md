# `2026-10-14-anonymous-c6d1e0ab-fd175df4` — `codetables-binary-linear` (`[171, 17, 70]_2`)

## What
Verified that object/opt_win_q2_n171_k17_d70.json (6,208 bytes, SHA-256 fd175df444fe56b8d6d2eb4007e72edacec2575e49ac048492f2035eff96e2b4) defines an explicit 17 x 171 generator matrix G over GF(2) of exact row rank 17 whose linear code [171, 17, 70]_2 has exact minimum Hamming distance d = 70 (with A_70 = 1092 minimum-weight codewords across all 131,071 nonzero codewords, verified identically by two independent full-codebook enumerators), strictly improving upon the live codetables.de lower bound d_lower = 69 (upper bound 76) by +1.

## Check It Yourself
```bash
bash verify-it-yourself/run_checks.sh
```

## Compared To
- **Markus Grassl's `codetables.de` (`http://www.codetables.de/BKLC/BKLC.php?q=2&n=171&k=17`, fetched `2026-10-14T10:24:01Z`, bulk SHA-256 `05ae81d4a6f4e57f9808a439567b097e96429db5b104a5251cb4048cbd1ff45d`)**:
  - Standing lower bound: `d_lower = 69` (upper bound `d_upper = 76`)
  - Our explicit generator matrix (`object/opt_win_q2_n171_k17_d70.json`): `d = 70` (`+1` improvement, `A_70 = 1092`)
- **Prior Literature**: Disjoint from `LinCodeEvolve` (`arXiv:2609.37056`, which covers only $q = 2, k \in [19, 22], n \in [170, 240]$).

## Not Claimed
- Does not claim optimality at the `codetables.de` upper bound `d_upper = 76` or improvements for other `(q, n, k)` cells in this package.

## Credits
- Reference bounds table maintained by Markus Grassl (`http://www.codetables.de/`).
