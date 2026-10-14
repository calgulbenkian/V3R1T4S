# `2026-10-14-anonymous-c6d1e0ab-c04fa003` — `cage-upper-bounds` (`[2, 11; 6]`-Mixed Graph, `N = 450`)

## What
Verified that object/mixed_z2_r11_g6_N450.json (39,066 bytes, SHA-256 c04fa003c1474a615f252960788061395ba80f6bf0681572cd048990467ead63) defines an explicit simple [2, 11; 6]-mixed graph on N = 450 vertices (every vertex having exact in-degree 2, out-degree 2, undirected degree 11, and mixed girth 6 verified by two independent shortest-cycle algorithms), strictly improving upon the standing upper bound 480 in Table 1 of Araujo-Pardo and Mendoza-Cadena (arXiv:2506.20003) by -30 vertices (Partial Win p2).

## Check It Yourself
```bash
bash verify-it-yourself/run_checks.sh
```

## Compared To
- **Araujo-Pardo and Mendoza-Cadena (`arXiv:2506.20003`, Table 1, fetched `2026-10-14T08:13:18Z`, SHA-256 `1b1cc422cd10a41255b96a03e4a5d337ddbfa0aa3759907e1be647f02537`)**:
  - Standing upper bound for `[2, 11; 6]`: `N = 480`
  - Jajcayova and Jajcay (2025) Theorem 3.6 bound: `N = 546`
  - Our explicit graph (`object/mixed_z2_r11_g6_N450.json`): `N = 450` (`-30` vertices vs Table 1, `-96` vs Jajcayova–Jajcay)

## Not Claimed
- Does not claim a classical undirected $(k, g)$-cage upper-bound improvement (Full Win); this submission claims Partial Win `p2` (improving a live upper-bound entry of the mixed-cage table `arXiv:2506.20003`).

## Credits
- Mixed-cage table and baseline bounds by Gabriela Araujo-Pardo and Lydia Mirabel Mendoza-Cadena (`arXiv:2506.20003`, `arXiv:2401.14768`).
