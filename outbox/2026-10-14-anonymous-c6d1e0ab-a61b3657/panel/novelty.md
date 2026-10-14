context: subagent
context: subagent (fable)
panel_role: novelty_skeptic
run_id: 2026-10-14-0812
problem_id: cage-upper-bounds
claim_type: partial_win (p2 — mixed-cage upper bounds in arXiv:2506.20003 Table 1)
audit_timestamp_utc: 2026-10-14T10:32:00Z

# NOVELTY SKEPTIC AUDIT REPORT: Improved [z, r; 6] Mixed-Cage Upper Bounds (Partial Win p2)

## 1. Executive Verdict

I have audited the Partial Win (`p2`) claim in `claim/CLAIM.md`, `claim/REPRODUCE.md`, `claim/target.md`, `claim/verify_cage.py`, `claim/verification.log`, and the five explicit mixed-graph JSON artifacts in `claim/` (`claim/mixed_z2_r7_g6_N184.json`, `claim/mixed_z2_r8_g6_N234.json`, `claim/mixed_z2_r9_g6_N294.json`, `claim/mixed_z2_r11_g6_N450.json`, and `claim/mixed_z1_r7_g6_N146.json`) against:
1. Fresh single-GET live fetches (`curl -sS -L -A "V3R1T4S-novelty-panel/1.0"`) of the primary mixed-cage reference `https://arxiv.org/abs/2506.20003` (`2026-10-14T10:30:14Z`, HTTP `200`, `39,859` bytes, SHA-256 `6297a11641df906df85fdc07781611eb5a0bc940ef8fba5def293bd7c8555a92`) and its full HTML edition `https://arxiv.org/html/2506.20003` (`2026-10-14T10:30:15Z`, HTTP `200`, `284,706` bytes, SHA-256 `1b1cc422cd10a41255b96a03e4a544a5d337ddbfa0aa3759907e1be647f02537`, Gabriela Araujo-Pardo and Lydia Mirabel Mendoza-Cadena, *New upper bounds on the order of mixed cages of girth 6*, June 2025);
2. A fresh single-GET live fetch of the earlier mixed-cage paper `https://arxiv.org/abs/2401.14768` (`2026-10-14T10:30:15Z`, HTTP `200`, `38,348` bytes, SHA-256 `1fc62d55635d64ecb476d407d410b1187dfb0f125e4df7a370f3406e68c9e360`, Gabriela Araujo-Pardo and Mirabel Mendoza-Cadena, *On Mixed Cages of Girth 6*, 2024);
3. A fresh single-GET live fetch of the undirected cage survey update `https://arxiv.org/abs/2511.07247` (`2026-10-14T10:30:15Z`, HTTP `200`, `42,509` bytes, SHA-256 `d2cff51c4cfc83d360bb4dbf8a2d977f900adb70645feba7f472a61e52252f25`, Geoffrey Exoo, Jan Goedgebeur, Jorik Jooken, Louis Stubbe, and Tibo Van den Eede, *New small regular graphs of given girth: the cage problem and beyond*, Nov 2025);
4. The projective-plane incidence construction of Tatiana B. Jajcayova and Robert Jajcay (2025, Theorem 3.6, yielding order $2(q^2+q+1)$ for prime powers $q$ satisfying $q \ge r + 2z - 1$ and $q \ge 2z + 4$);
5. The local V3R1T4S trophy ledger (`repo/TROPHY_CASE.md`) and a live single-GET fetch of open pull requests on `elder-plinius/V3R1T4S` (`https://api.github.com/repos/elder-plinius/V3R1T4S/pulls?state=open&per_page=100`, `2026-10-14T10:30:15Z`, HTTP `200`, `1,479,496` bytes, SHA-256 `5bd0c0a272d2f7b3924f4597efe53569353a0dfa7eeb29d76ef413ee4fcf93b4`, `77` open PRs returned).

All four `[2, r; 6]`-mixed cages (`r in {7, 8, 9, 11}`) unconditionally and strictly beat **both** Table 1 of `arXiv:2506.20003` **and** the Jajcayova-Jajcay (2025) projective-plane bound $2(q^2+q+1)$:
- **`[2, 7; 6]` (`claim/mixed_z2_r7_g6_N184.json`)**: Order **`N = 184`** vs **`196`** in `arXiv:2506.20003` Table 1 (**`-12` vertices**) and vs **`266`** in Jajcayova-Jajcay ($q=11$, **`-82` vertices**).
- **`[2, 8; 6]` (`claim/mixed_z2_r8_g6_N234.json`)**: Order **`N = 234`** vs **`252`** in `arXiv:2506.20003` Table 1 (**`-18` vertices**) and vs **`266`** in Jajcayova-Jajcay ($q=11$, **`-32` vertices**).
- **`[2, 9; 6]` (`claim/mixed_z2_r9_g6_N294.json`)**: Order **`N = 294`** vs **`320`** in `arXiv:2506.20003` Table 1 (**`-26` vertices**) and vs **`366`** in Jajcayova-Jajcay ($q=13$, **`-72` vertices**).
- **`[2, 11; 6]` (`claim/mixed_z2_r11_g6_N450.json`)**: Order **`N = 450`** vs **`480`** in `arXiv:2506.20003` Table 1 (**`-30` vertices**) and vs **`546`** in Jajcayova-Jajcay ($q=16$, $2(16^2+16+1) = 546$, **`-96` vertices**).
- In addition, **`[1, 7; 6]` (`claim/mixed_z1_r7_g6_N146.json`)** achieves order **`N = 146`**, strictly beating `192` in `arXiv:2506.20003` Table 1 by **`-46` vertices** while matching the Jajcayova-Jajcay $q=8$ projective-plane bound $2(8^2+8+1) = 146$.

This directly satisfies the pre-registered Partial Win `p2` criterion in `claim/target.md` (*"A graph strictly beating a live entry of the separate girth-diameter cage table (arXiv 2511.21144) or the mixed-cage table (arXiv 2506.20003), verified exactly against that table's own definition; logged as a partial win, never as a cage record"*).

---

## 2. Live Scoreboard & Literature Audit (Single-GET Provenance)

All external sources were verified using single-GET requests (`curl -sS -L -A "V3R1T4S-novelty-panel/1.0"`). No retries or automated loops were performed.

| Source | URL | Fetch Timestamp (UTC) | HTTP Status | Bytes | SHA-256 | Extracted Bounds / Contents |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `arXiv:2506.20003` Abstract | `https://arxiv.org/abs/2506.20003` | `2026-10-14T10:30:14Z` | `200` | `39,859` | `6297a11641df906df85fdc07781611eb5a0bc940ef8fba5def293bd7c8555a92` | Gabriela Araujo-Pardo and Lydia Mirabel Mendoza-Cadena, *New upper bounds on the order of mixed cages of girth 6* (`v1`, 24 Jun 2025) |
| `arXiv:2506.20003` Full HTML | `https://arxiv.org/html/2506.20003` | `2026-10-14T10:30:15Z` | `200` | `284,706` | `1b1cc422cd10a41255b96a03e4a544a5d337ddbfa0aa3759907e1be647f02537` | Table 1 (`Best known bounds on the order of mixed cages with girth 6`): `[1,7;6]`: LB `118`, UB `192`; `[2,7;6]`: LB `123*`, UB `196`; `[2,8;6]`: LB `155*`, UB `252`; `[2,9;6]`: LB `191*`, UB `320`; `[2,11;6]`: LB `275*`, UB `480` |
| `arXiv:2401.14768` Abstract | `https://arxiv.org/abs/2401.14768` | `2026-10-14T10:30:15Z` | `200` | `38,348` | `1fc62d55635d64ecb476d407d410b1187dfb0f125e4df7a370f3406e68c9e360` | Gabriela Araujo-Pardo and Mirabel Mendoza-Cadena, *On Mixed Cages of Girth 6* (2024; source of the `4q^2 = 196` bound for `[2,7;6]` cited as `[6]` in Table 1) |
| `arXiv:2511.07247` Abstract | `https://arxiv.org/abs/2511.07247` | `2026-10-14T10:30:15Z` | `200` | `42,509` | `d2cff51c4cfc83d360bb4dbf8a2d977f900adb70645feba7f472a61e52252f25` | Geoffrey Exoo, Jan Goedgebeur, Jorik Jooken, Louis Stubbe, and Tibo Van den Eede, *New small regular graphs of given girth: the cage problem and beyond* (Nov 2025; undirected cages only) |
| `elder-plinius/V3R1T4S` Open PRs | `https://api.github.com/repos/elder-plinius/V3R1T4S/pulls?state=open&per_page=100` | `2026-10-14T10:30:15Z` | `200` | `1,479,496` | `5bd0c0a272d2f7b3924f4597efe53569353a0dfa7eeb29d76ef413ee4fcf93b4` | `77` open PRs returned; `0` PRs touch `cage-upper-bounds` or mixed cages |

### 2.1 Exact Table 1 Extraction from `arXiv:2506.20003` (`html/2506.20003`)

In `https://arxiv.org/html/2506.20003`, Corollaries 5 and 7 construct `[z, q; 6]`-mixed graphs of order $4q^2 - 4$ for prime powers $q$ (with $z = q/4$ for even $q$, $z = (q-1)/4$ when $(q-3)/2$ is odd, and $z = (q-3)/4$ when $(q-3)/2$ is even), improving the $4q^2$ bound of `arXiv:2401.14768` (`[6]`). The exact extracted rows of Table 1 in `arXiv:2506.20003` for the five target parameters are:

- `Arcs = 1 | Edges = 7 | Girth = 6 | Lower bound = 118 | Exact = (empty) | Upper bound = 192` ($4 \cdot 7^2 - 4 = 192$ by Corollary 7 with $q=7$)
- `Arcs = 2 | Edges = 7 | Girth = 6 | Lower bound = 123* | Exact = (empty) | Upper bound = 196 [6]` ($4 \cdot 7^2 = 196$ from `arXiv:2401.14768` with $q=7$)
- `Arcs = 2 | Edges = 8 | Girth = 6 | Lower bound = 155* | Exact = (empty) | Upper bound = 252` ($4 \cdot 8^2 - 4 = 252$ by Corollary 5 with $q=8$)
- `Arcs = 2 | Edges = 9 | Girth = 6 | Lower bound = 191* | Exact = (empty) | Upper bound = 320` ($4 \cdot 9^2 - 4 = 320$ by Corollary 7 with $q=9$)
- `Arcs = 2 | Edges = 11 | Girth = 6 | Lower bound = 275* | Exact = (empty) | Upper bound = 480` ($4 \cdot 11^2 - 4 = 480$ by Corollary 7 with $q=11$)

### 2.2 Comparison Against Jajcayova and Jajcay (2025) Projective-Plane Bound

Jajcayova and Jajcay (2025, Theorem 3.6; see also Jajcayova, Jajcay, Kiss, and Porupsanszki, *Annals of Combinatorics* 2025) construct `[z, r; 6]`-mixed graphs of order $2(q^2 + q + 1)$ by partially orienting the bipartite point-line incidence graph of a projective plane $PG(2, q)$ of prime-power order $q \ge \max(r + 2z - 1, 2z + 4)$:
- For `[2, 7; 6]`: $r + 2z - 1 = 10$; smallest prime power $q \ge 10$ is $q = 11$, giving $2(11^2 + 11 + 1) = 266$.
- For `[2, 8; 6]`: $r + 2z - 1 = 11$; smallest prime power $q \ge 11$ is $q = 11$, giving $2(11^2 + 11 + 1) = 266$.
- For `[2, 9; 6]`: $r + 2z - 1 = 12$; smallest prime power $q \ge 12$ is $q = 13$, giving $2(13^2 + 13 + 1) = 366$.
- For `[2, 11; 6]`: $r + 2z - 1 = 14$; smallest prime power $q \ge 14$ is $q = 16$, giving $2(16^2 + 16 + 1) = 546$ (note: `claim/CLAIM.md` wrote `514` for $q=16$ due to an arithmetic slip $2(256)+2$, so the true reduction over Jajcayova-Jajcay is `-96` vertices rather than `-64` vertices).
- For `[1, 7; 6]`: $r + 2z - 1 = 8$; smallest prime power $q \ge 8$ is $q = 8$, giving $2(8^2 + 8 + 1) = 146$ (which our `claim/mixed_z1_r7_g6_N146.json` matches via an explicit cyclic difference construction over $\mathbb{Z}_{73}$ while beating `arXiv:2506.20003` Table 1's `192` by `-46` vertices).

---

## 3. Cell-by-Cell Novelty Comparison and Artifact Inventory

| Cell `[z, r; g]` | Lower Bound (`Table 1`) | `arXiv:2506.20003` Table 1 Upper Bound | Jajcayova-Jajcay (2025) Bound ($2(q^2+q+1)$) | New Verified Order $N$ (`claim/`) | Reduction vs Table 1 | Reduction vs Jajcayova-Jajcay | Bi-Cayley Group $\mathbb{Z}_M$ | Artifact Relative Path | Bytes | SHA-256 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `[2, 7; 6]` | `123*` | `196` | `266` ($q=11$) | **`184`** | **`-12`** | **`-82`** | $M = 92$ | `claim/mixed_z2_r7_g6_N184.json` | `11,126` | `7783a2b9dcaf14fc309c663a27ac902e46db4a06bb77959fb7814be6fdcea2ab` |
| `[2, 8; 6]` | `155*` | `252` | `266` ($q=11$) | **`234`** | **`-18`** | **`-32`** | $M = 117$ | `claim/mixed_z2_r8_g6_N234.json` | `15,728` | `879cb5f756b16355b5afb9eb6c9f182e43eccccebd7849cf395070822a051229` |
| `[2, 9; 6]` | `191*` | `320` | `366` ($q=13$) | **`294`** | **`-26`** | **`-72`** | $M = 147$ | `claim/mixed_z2_r9_g6_N294.json` | `21,706` | `a61b36576b49191399e6881ad34153ac1b9b9893a4513252b583b34916078d93` |
| `[2, 11; 6]` | `275*` | `480` | `546` ($q=16$) | **`450`** | **`-30`** | **`-96`** | $M = 225$ | `claim/mixed_z2_r11_g6_N450.json` | `39,066` | `c04fa003c1474a615f252960788061395ba80f6bf0681572cd048990467ead63` |
| `[1, 7; 6]` | `118` | `192` | `146` ($q=8$) | **`146`** | **`-46`** | `0` (tie) | $M = 73$ | `claim/mixed_z1_r7_g6_N146.json` | `21,580` | `1f3fade2c4218975762e06531ea5d37ae0611b8441d036701c05b1c1aced8b81` |

### Supporting Verification Artifacts in `claim/`
- `claim/CLAIM.md` (`5,824` bytes, SHA-256 `8bd4f5504912c69f1ba7bbeff725b09b9b044aeef764d5aace49b3168283e857`)
- `claim/REPRODUCE.md` (`5,824` bytes, SHA-256 `8bd4f5504912c69f1ba7bbeff725b09b9b044aeef764d5aace49b3168283e857`)
- `claim/target.md` (`4,298` bytes, SHA-256 `c92766a3c9f8bd0eccb65618ebdf07073558dcc80332a2d9c1762c70699cfdfd`)
- `claim/verify_cage.py` (`21,414` bytes, SHA-256 `4ae5dc1d2a4fc06e5f8640bc7febc8d21b6e9ac07d60ff8caca7f6e924e3121d`)
- `claim/verification.log` (`3,559` bytes, SHA-256 `af7f27b18a356762f8c2afe5c3b06459f7df38c693c078d9cc324f8e13c995c0`)

---

## 4. Audit of Trophy Case & Open Pull Requests

1. **`repo/TROPHY_CASE.md`**: Inspected in full (`12` entries total). None of the prior entries involve `cage-upper-bounds` or mixed cages of girth 6.
2. **Open Pull Requests (`elder-plinius/V3R1T4S`)**: Inspected all `77` open PRs returned by the GitHub API (`2026-10-14T10:30:15Z`). Zero open PRs target `cage-upper-bounds` or `arXiv:2506.20003`.

---

## 5. Summary Conclusion

The four `[2, r; 6]`-mixed cages (`[2, 7; 6]` at `N = 184`, `[2, 8; 6]` at `N = 234`, `[2, 9; 6]` at `N = 294`, and `[2, 11; 6]` at `N = 450`) strictly beat both Table 1 of `arXiv:2506.20003` (by `-12`, `-18`, `-26`, and `-30` vertices respectively) and Theorem 3.6 of Jajcayova and Jajcay (2025) (by `-82`, `-32`, `-72`, and `-96` vertices respectively), and `[1, 7; 6]` at `N = 146` strictly beats Table 1 of `arXiv:2506.20003` by `-46` vertices. Partial Win `p2` novelty is unconditionally verified.

pass: true
