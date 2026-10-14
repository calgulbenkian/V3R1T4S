# `2026-10-14-anonymous-c6d1e0ab-916098a5` — `snake-coil-in-the-box` (`Q_13` `symmetric_coil`, `L = 2870`)

## What
Verified that object/sym_coil_Q13_2870.txt (2,871 bytes, SHA-256 916098a5643395c31ff6ee83b41ba473c9c177fda1b1a6e52689f9ce1ce66eea) defines a valid symmetric induced cycle (coil) in the 13-dimensional hypercube Q_13 of edge length L = 2870 invariant under the minortriad half-period symmetry (steps[:1435] == steps[1435:]), strictly improving upon the live minortriad.com symmetric-coil record L = 2830 by +40 edges (Partial Win p1).

## Check It Yourself
```bash
bash verify-it-yourself/run_checks.sh
```

## Compared To
- **Primary Scoreboard (`https://www.minortriad.com/snake/`, fetched `2026-10-14T10:14:48Z`, SHA-256 `af45d6499dcae6cb6d3e1942c5ccd0ab8159c7755dec1667e097a1859dfcebb2`)** and published repositories (`Caltech-Snake-Pit/snakes-in-a-box`, `tommyet/snakes`, `williamtoner/SnakeBox`):
  - Standing bound: `L = 2830`
  - Our certificate (`object/sym_coil_Q13_2870.txt`): `L = 2870` (Q13 symmetric coil of length L = 2870 vs 2830 live minortriad.com record (+40 edges, partial win p1))

## Not Claimed
- Does not claim a strictly longer unrestricted snake or coil in $Q_9..Q_{13}$ (which would be a Full Win); this submission claims Partial Win `p1` as defined in `target.md`.

## Credits
- Reference records and tables by Wynn (`minortriad.com`), Orland-Fagan et al. (`arXiv:2607.15270v3`), Thomas Taylor (`arXiv:2609.27483`), and William Toner (`williamtoner/SnakeBox`).
