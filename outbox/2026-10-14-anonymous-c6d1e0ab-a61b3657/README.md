# `2026-10-14-anonymous-c6d1e0ab-a61b3657` — `cage-upper-bounds` (`[2, 9; 6]`-Mixed Graph, `N = 294`)

## What
Verified that object/mixed_z2_r9_g6_N294.json (21,706 bytes, SHA-256 a61b36576b49191399e6881ad34153ac1b9b9893a4513252b583b34916078d93) defines an explicit simple [2, 9; 6]-mixed graph on N = 294 vertices (every vertex having exact in-degree 2, out-degree 2, undirected degree 9, and mixed girth 6 verified by two independent shortest-cycle algorithms), strictly improving upon the standing upper bound 320 in Table 1 of Araujo-Pardo and Mendoza-Cadena (arXiv:2506.20003) by -26 vertices (Partial Win p2).

## Check It Yourself
```bash
bash verify-it-yourself/run_checks.sh
```

## Compared To
- **Araujo-Pardo and Mendoza-Cadena (`arXiv:2506.20003`, Table 1, fetched `2026-10-14T08:13:18Z`, SHA-256 `1b1cc422cd10a41255b96a03e4a5d337ddbfa0aa3759907e1be647f02537`)**:
  - Standing upper bound for `[2, 9; 6]`: `N = 320`
  - Jajcayova and Jajcay (2025) Theorem 3.6 bound: `N = 366`
  - Our explicit graph (`object/mixed_z2_r9_g6_N294.json`): `N = 294` (`-26` vertices vs Table 1, `-72` vs Jajcayova–Jajcay)

## Not Claimed
- Does not claim a classical undirected $(k, g)$-cage upper-bound improvement (Full Win); this submission claims Partial Win `p2` (improving a live upper-bound entry of the mixed-cage table `arXiv:2506.20003`).

## Credits
- Mixed-cage table and baseline bounds by Gabriela Araujo-Pardo and Lydia Mirabel Mendoza-Cadena (`arXiv:2506.20003`, `arXiv:2401.14768`).
