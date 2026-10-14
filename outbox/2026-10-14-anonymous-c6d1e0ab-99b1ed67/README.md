# `2026-10-14-anonymous-c6d1e0ab-99b1ed67` — `snake-coil-in-the-box` (`Q_12` `symmetric_coil`, `L = 1450`)

## What
Verified that object/sym_coil_Q12_1450.txt (1,451 bytes, SHA-256 99b1ed6796d7742edbc672164214e4bc6b3a9e0ccd7b4d62a9159936d9339606) defines a valid symmetric induced cycle (coil) in the 12-dimensional hypercube Q_12 of edge length L = 1450 invariant under the minortriad half-period symmetry (steps[:725] == steps[725:]), strictly improving upon the live minortriad.com symmetric-coil record L = 1434 by +16 edges (Partial Win p1).

## Check It Yourself
```bash
bash verify-it-yourself/run_checks.sh
```

## Compared To
- **Primary Scoreboard (`https://www.minortriad.com/snake/`, fetched `2026-10-14T10:14:48Z`, SHA-256 `af45d6499dcae6cb6d3e1942c5ccd0ab8159c7755dec1667e097a1859dfcebb2`)** and published repositories (`Caltech-Snake-Pit/snakes-in-a-box`, `tommyet/snakes`, `williamtoner/SnakeBox`):
  - Standing bound: `L = 1434`
  - Our certificate (`object/sym_coil_Q12_1450.txt`): `L = 1450` (Q12 symmetric coil of length L = 1450 vs 1434 live minortriad.com record (+16 edges, partial win p1))

## Not Claimed
- Does not claim a strictly longer unrestricted snake or coil in $Q_9..Q_{13}$ (which would be a Full Win); this submission claims Partial Win `p1` as defined in `target.md`.

## Credits
- Reference records and tables by Wynn (`minortriad.com`), Orland-Fagan et al. (`arXiv:2607.15270v3`), Thomas Taylor (`arXiv:2609.27483`), and William Toner (`williamtoner/SnakeBox`).
