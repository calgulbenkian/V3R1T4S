# `2026-10-14-anonymous-c6d1e0ab-07292e7f` — `codetables-binary-linear` (`[174, 17, 72]_2`)

## What
Verified that object/opt_win_q2_n174_k17_d72.json (6,313 bytes, SHA-256 07292e7fb3a5377aa924d70118c0c8a409df6cf4b2641584d1aa0a765a298218) defines an explicit 17 x 174 generator matrix G over GF(2) of exact row rank 17 whose linear code [174, 17, 72]_2 has exact minimum Hamming distance d = 72 (with A_72 = 3154 minimum-weight codewords across all 131,071 nonzero codewords, verified identically by two independent full-codebook enumerators), strictly improving upon the live codetables.de lower bound d_lower = 71 (upper bound 78) by +1.

## Check It Yourself
```bash
bash verify-it-yourself/run_checks.sh
```

## Compared To
- **Markus Grassl's `codetables.de` (`http://www.codetables.de/BKLC/BKLC.php?q=2&n=174&k=17`, fetched `2026-10-14T10:24:01Z`, bulk SHA-256 `05ae81d4a6f4e57f9808a439567b097e96429db5b104a5251cb4048cbd1ff45d`)**:
  - Standing lower bound: `d_lower = 71` (upper bound `d_upper = 78`)
  - Our explicit generator matrix (`object/opt_win_q2_n174_k17_d72.json`): `d = 72` (`+1` improvement, `A_72 = 3154`)
- **Prior Literature**: Disjoint from `LinCodeEvolve` (`arXiv:2609.37056`, which covers only $q = 2, k \in [19, 22], n \in [170, 240]$).

## Not Claimed
- Does not claim optimality at the `codetables.de` upper bound `d_upper = 78` or improvements for other `(q, n, k)` cells in this package.

## Credits
- Reference bounds table maintained by Markus Grassl (`http://www.codetables.de/`).
