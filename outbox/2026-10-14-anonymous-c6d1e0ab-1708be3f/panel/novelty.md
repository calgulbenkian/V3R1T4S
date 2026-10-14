context: subagent
context: subagent (fable)
panel_role: novelty_skeptic
run_id: 2026-10-14-0740
problem_id: snake-coil-in-the-box
claim_type: partial_win (p1, p2, p3)
audit_timestamp_utc: 2026-10-14T10:25:00Z

# NOVELTY SKEPTIC AUDIT REPORT: Snake-in-the-Box and Coil-in-the-Box Records in Q_10..Q_14 (p1, p2, p3)

## 1. Executive Verdict

I have audited the novelty claims in `claim/CLAIM.md`, `claim/REPRODUCE.md`, `claim/target.md`, `claim/verify_snake.py`, `claim/seeds/minortriad_records.json`, and all 13 sequence transition files in `claim/` against:
1. A fresh single-GET live fetch of the canonical Snake-in-the-Box and Coil-in-the-Box scoreboard maintained by Forrest J. Echols at `https://www.minortriad.com/snake/` (`2026-10-14T10:22:37Z`, HTTP `200`, SHA-256 `af45d6499dcae6cb6d3e1942c5ccd0ab8159c7755dec1667e097a1859dfcebb2`), as well as the frozen pre-registration snapshot in `claim/seeds/minortriad_records.json` (`20,673` bytes, SHA-256 `4aac8e5704c2a667f0912e1683a5b78f2909fada5b06cc4ea94a79534de133fb`);
2. A fresh single-GET live fetch of the Caltech Math-AI repository `https://raw.githubusercontent.com/Math-AI-Caltech/Snake-in-the-Box/main/README.md` (`2026-10-14T10:22:39Z`, HTTP `200`, corresponding to Fagan, Kipf, Sergazinov, Poggio, Gukov, and Garg, arXiv:2607.15270, July 2026);
3. A fresh single-GET live fetch of William Toner's repository `https://raw.githubusercontent.com/williamtoner/SnakeBox/main/README.md` (`2026-10-14T10:22:41Z`, HTTP `200`, `2,510` bytes, SHA-256 `67471bef48b4170eeacf0cf8c9240c1f3b9d2d6bb694a408b77fa8e03a45e43a`, updated Oct 12, 2026) and its transition files `q13_2946.txt` (SHA-256 `56676e1993ab2d74c03a3ebe2e5668194379f2bd79839689e0b0e0daec79f795`) and `q14_5850.txt` (SHA-256 `41ba6cebbc8bc8d029cfb93ae22f6a746a8bbb1fa99efca00591c9444606ee28`);
4. A fresh single-GET live fetch of Tom Taylor's repository `https://raw.githubusercontent.com/tommyet/snakes/master/README.md` (`2026-10-14T10:24:02Z`, HTTP `200`, `1,466` bytes, SHA-256 `d75567ac4383f6f5e30396e740e7b0765bc3cfffcf94aa3b28ff58bed201c132`, corresponding to Tom Taylor, arXiv:2609.27483, Sep 2026);
5. The local V3R1T4S trophy ledger (`repo/TROPHY_CASE.md`) and a live fetch of open pull requests on `elder-plinius/V3R1T4S` (`https://api.github.com/repos/elder-plinius/V3R1T4S/pulls?state=open&per_page=100`, `2026-10-14T10:22:43Z`, HTTP `200`, `77` open PRs returned);
6. Recent 2024-2026 literature on induced paths and cycles in hypercubes (Meyerson et al. 2015; Allison, Paulusma, Smith 2022; Fagan et al. arXiv:2607.15270, July 2026; Taylor arXiv:2609.27483, Sep 2026; Echols 2026; Itty 2026; Toner Oct 2026).

All three pre-registered Partial Win categories in `claim/target.md` are genuinely novel, strictly establish new world records or non-isomorphic record constructions, and have zero overlap with prior entries in `repo/TROPHY_CASE.md` or open pull requests:
- **Partial Win `p1` (Symmetric-Coil World Records in $Q_{12}$ and $Q_{13}$,Tracked on `minortriad.com/snake`)**:
  - $Q_{12}$ (`sc12`): `claim/sym_coil_Q12_1450.txt` achieves length `L = 1450` (period-2, index `m = 725`, XOR-sum `3562` of Hamming weight `6`), strictly beating the `minortriad.com/snake` world record `sc12 = 1434` (`Echols2026g`) by `+16` edges.
  - $Q_{13}$ (`sc13`): `claim/sym_coil_Q13_2870.txt` achieves length `L = 2870` (period-2, index `m = 1435`, XOR-sum `4035` of Hamming weight `8`), strictly beating the `minortriad.com/snake` world record `sc13 = 2830` (`Echols2026g`) by `+40` edges. A secondary independent construction `claim/sym_coil_Q13_2846.txt` achieves `L = 2846` (`+16` edges over `2830`).
- **Partial Win `p2` ($Q_{14}$ Unrestricted Coil and Snake World Records)**:
  - $Q_{14}$ Coil (`co14`): `claim/coil_Q14_5854.txt` achieves an unrestricted induced cycle (coil) in $Q_{14}$ of length `L = 5854` edges (and is additionally period-2 symmetric with half-coil length `m = 2927`), strictly beating the best published $Q_{14}$ coil record `5750` (Tom Taylor, arXiv:2609.27483, Sep 2026) by `+104` edges, and even strictly beating the best prior $Q_{14}$ open-snake record `5850` (William Toner, Oct 12, 2026) by `+4` edges despite satisfying the stricter closed-cycle constraint.
  - $Q_{14}$ Snake (`sn14`): `claim/snake_Q14_5854.txt` achieves an induced path (snake) in $Q_{14}$ of length `L = 5854` edges, strictly beating William Toner's Oct 12, 2026 world record of `5850` edges (`q14_5850.txt`) by `+4` edges and Tom Taylor's Sep 2026 preprint record of `5844` edges (arXiv:2609.27483) by `+10` edges.
- **Partial Win `p3` (7 Strictly Non-Isomorphic Equal-Record Snakes and Coils in $Q_{10}..Q_{13}$)**:
  - 7 transition sequences (`claim/inequiv_co10_374.txt`, `claim/inequiv_co11_740.txt`, `claim/inequiv_co12_1468.txt`, `claim/inequiv_co13_2930.txt`, `claim/inequiv_sn11_750.txt`, `claim/inequiv_sn12_1480.txt`, `claim/inequiv_sn13_2946.txt`) match the exact current `minortriad.com/snake` world-record lengths (`co10=374`, `co11=740`, `co12=1468`, `co13=2930`, `sn11=750`, `sn12=1480`, `sn13=2946`) while being provably non-isomorphic under the full hypercube automorphism group $B_d = S_d \ltimes \mathbb{Z}_2^d$ (including cyclic shifts and reversals) to every published record on `minortriad.com/snake` and `williamtoner/SnakeBox`, certified via distinct sorted coordinate transition count profiles and gap spectrum distributions.

---

## 2. Live Scoreboard & Literature Audit (Single-GET Provenance)

All external sources were verified using single-GET requests (`curl -sS -L -A "V3R1T4S-novelty-panel/1.0"`). No retries or automated loops were performed.

| Source | URL | Fetch Timestamp (UTC) | HTTP Status | Bytes | SHA-256 | Relevant Extracted Bounds |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `minortriad.com/snake` | `https://www.minortriad.com/snake/` | `2026-10-14T10:22:37Z` | `200` | `83,682` | `af45d6499dcae6cb6d3e1942c5ccd0ab8159c7755dec1667e097a1859dfcebb2` | `sc9=186`, `sc10=370`, `sc11=730`, `sc12=1434` (`Echols2026g`), `sc13=2830` (`Echols2026g`); `co9=192`, `co10=374` (`Fagan2026`), `co11=740` (`Echols2026e`), `co12=1468` (`Echols2026d`), `co13=2930` (`Echols2026g`); `sn9=191`, `sn10=379`, `sn11=750` (`Echols2026g`), `sn12=1480` (`Itty2026a`), `sn13=2946` (`Toner2026a`) |
| `Math-AI-Caltech/Snake-in-the-Box` | `https://raw.githubusercontent.com/Math-AI-Caltech/Snake-in-the-Box/main/README.md` | `2026-10-14T10:22:39Z` | `200` | `3,891` | `1a0c58b67b1482c1e6e8f15c99c8e7bc80929a2eb1e99a4d546fb82f9d9562bc` | Paper (`arXiv:2607.15270`): `sn9=191..sn13=2924`, `co9=192..co13=2916`, `sc10=370`, `sc11=730`; Subsequent bounds noted: `sn11=750` (Echols), `sn12=1480` and `sn13=2934` (Itty) |
| `williamtoner/SnakeBox` README | `https://raw.githubusercontent.com/williamtoner/SnakeBox/main/README.md` | `2026-10-14T10:22:41Z` | `200` | `2,510` | `67471bef48b4170eeacf0cf8c9240c1f3b9d2d6bb694a408b77fa8e03a45e43a` | `Q13` snake `2946` edges (11 Oct 2026, `q13_2946.txt`), `Q14` snake `5850` edges (12 Oct 2026, `q14_5850.txt`) |
| `tommyet/snakes` README | `https://raw.githubusercontent.com/tommyet/snakes/master/README.md` | `2026-10-14T10:24:02Z` | `200` | `1,466` | `d75567ac4383f6f5e30396e740e7b0765bc3cfffcf94aa3b28ff58bed201c132` | Paper (`arXiv:2609.27483`, Sep 2026): `Q13` snake `2,938`, `Q14` snake `5,844`, `Q14` coil `5,750` |
| `elder-plinius/V3R1T4S` Open PRs | `https://api.github.com/repos/elder-plinius/V3R1T4S/pulls?state=open&per_page=100` | `2026-10-14T10:22:43Z` | `200` | `198,412` | `786521df8a308c9d0ec0e1f8493802f7a2335982ca16c9f9e8f17c8d07bc2ab3` | `77` open PRs returned; `0` PRs touch `snake-coil-in-the-box` |

### 2.1 Detailed Literature Audit (2024-2026)

1. **Fagan, Kipf, Sergazinov, Poggio, Gukov, and Garg (`arXiv:2607.15270`, July 2026)**, *"Long Snakes and Coils in the Box via Transformer-Guided Search"*:
   - Improved lower bounds in $Q_9..Q_{13}$ to `sn9=191`, `sn10=379`, `sn11=746`, `sn12=1476`, `sn13=2924` for snakes; `co9=192`, `co10=374`, `co11=734`, `co12=1466`, `co13=2916` for coils; and `sc10=370`, `sc11=730` for symmetric coils. Did not report constructions in $Q_{14}$ or symmetric coils above `1434` in $Q_{12}$ or `2830` in $Q_{13}$.
2. **Forrest J. Echols (`minortriad.com/snake`, July-Oct 2026)**:
   - Maintains the primary online scoreboard tracking `sn`, `co`, and `sc` for $d = 1..13$. As verified live at `2026-10-14T10:22:37Z`, the current scoreboard entries for $d = 10..13$ are:
     - Symmetric coils: `sc10 = 370` (`Fagan2026`), `sc11 = 730` (`Echols2026f`), `sc12 = 1434` (`Echols2026g`), `sc13 = 2830` (`Echols2026g`).
     - Coils: `co10 = 374` (`Fagan2026`), `co11 = 740` (`Echols2026e`), `co12 = 1468` (`Echols2026d`), `co13 = 2930` (`Echols2026g`).
     - Snakes: `sn10 = 379` (`Fagan2026`), `sn11 = 750` (`Echols2026g`), `sn12 = 1480` (`Itty2026a`), `sn13 = 2946` (`Toner2026a`).
3. **Tom Taylor (`arXiv:2609.27483`, Sep 2026; `github.com/tommyet/snakes`)**, *"Finding Long Snakes and Coils in Larger Hypercubes"*:
   - Established `sn13 = 2938`, `sn14 = 5844`, and `co14 = 5750` (stored locally in `claim/seeds/taylor_snake_Q13.json`, `claim/seeds/taylor_snake_Q14.json`, `claim/seeds/taylor_coil_Q14.json`).
4. **William Toner (`github.com/williamtoner/SnakeBox`, Oct 11-12, 2026)**:
   - Established `sn13 = 2946` (11 Oct 2026, already reflected on `minortriad.com/snake` as `Toner2026a`) and `sn14 = 5850` (12 Oct 2026, `q14_5850.txt`). Did not report any $Q_{14}$ coil or symmetric coils in $Q_{12}..Q_{14}$.

---

## 3. Cell-by-Cell Novelty Comparison and Artifact Inventory

### 3.1 Partial Win `p1` (Symmetric-Coil World Records in $Q_{12}$ and $Q_{13}$)

| Dimension $d$ | Category | `minortriad.com/snake` Prior Record | Prior Holder | New Record (`claim/`) | Improvement | Period / Index $m$ | Artifact Relative Path | Bytes | SHA-256 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $Q_{12}$ | Symmetric Coil (`sc12`) | `1434` | `Echols2026g` | **`1450`** | **`+16`** | $k=2$, $m=725$ | `claim/sym_coil_Q12_1450.txt` | `1,451` | `99b1ed6796d7742edbc672164214e4bc6b3a9e0ccd7b4d62a9159936d9339606` |
| $Q_{13}$ | Symmetric Coil (`sc13`) | `2830` | `Echols2026g` | **`2870`** | **`+40`** | $k=2$, $m=1435$ | `claim/sym_coil_Q13_2870.txt` | `2,871` | `916098a5643395c31ff6ee83b41ba473c9c177fda1b1a6e52689f9ce1ce66eea` |
| $Q_{13}$ | Symmetric Coil (`sc13`, secondary) | `2830` | `Echols2026g` | **`2846`** | **`+16`** | $k=2$, $m=1423$ | `claim/sym_coil_Q13_2846.txt` | `2,847` | `c625b96ed05fc23149baddf52a8584742235c47c5d75010cffb3054f9a094853` |

### 3.2 Partial Win `p2` ($Q_{14}$ Coil and Snake World Records)

| Dimension $d$ | Category | Best Prior Published Bound | Prior Holder & Source | New Record (`claim/`) | Improvement | Additional Properties | Artifact Relative Path | Bytes | SHA-256 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $Q_{14}$ | Unrestricted Coil (`co14`) | `5750` | Tom Taylor (`arXiv:2609.27483`, Sep 2026) | **`5854`** | **`+104`** | Also a period-2 symmetric coil (`sc14 = 5854`, $m = 2927$, derived by doubling `claim/coil_Q13_2928.txt`, `2,929`B, SHA-256 `479db30f00a1963a746e2cff12972663d06fbd98e74192c185184af339e68c67`) | `claim/coil_Q14_5854.txt` | `5,855` | `508e47a18fd5083e40dd391b22f8df564f02cc9295af99977ac17e371e26b3c7` |
| $Q_{14}$ | Unrestricted Snake (`sn14`) | `5850` (`5844` preprint) | William Toner (`SnakeBox`, Oct 12, 2026) / Tom Taylor (`arXiv:2609.27483`, Sep 2026) | **`5854`** | **`+4`** vs Toner (`+10` vs Taylor) | Open chordless path in $Q_{14}$ | `claim/snake_Q14_5854.txt` | `5,855` | `47e5e3f6ef0d9d68065090f8749a15281151755cf453495da3669b4336b61935` |

### 3.3 Partial Win `p3` (7 Strictly Non-Isomorphic Equal-Record Constructions in $Q_{10}..Q_{13}$)

Each of the 7 constructions below matches the exact current `minortriad.com/snake` world record while possessing a strictly distinct hypercube-automorphism invariant (sorted coordinate transition frequency profile or cyclic coordinate gap spectrum) from the corresponding published record in `claim/seeds/minortriad_records.json` and `claim/seeds/toner_q13_2946.txt`:

| Record Key | Dimension & Type | World-Record Length $L$ | Published Reference Key | Inequivalence Invariant | Artifact Relative Path | Bytes | SHA-256 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `co10` | $Q_{10}$ Coil | `374` | `Fagan2026` | Distinct cyclic coordinate gap spectrum (`9` coordinates differ in gap multiset) | `claim/inequiv_co10_374.txt` | `375` | `f1a736ab0fcc62757d46850b884bcd6c80460bebced6d2f25c6eaef1d5380755` |
| `co11` | $Q_{11}$ Coil | `740` | `Echols2026e` | Sorted transition count profile `[64,66,66,66,66,68,68,68,68,68,72]` vs `[64,64,66,66,66,68,68,68,68,70,72]` | `claim/inequiv_co11_740.txt` | `741` | `3f22401b0f8250eccca65436ed4564f858bbb58e76e16da4dee6a77e5600b42d` |
| `co12` | $Q_{12}$ Coil | `1468` | `Echols2026d` | Sorted transition count profile `[116,120,120,122,122,122,122,124,124,124,126,126]` vs `[116,120,122,122,122,122,122,122,124,124,126,126]` | `claim/inequiv_co12_1468.txt` | `1,469` | `a4b75c268608c66ec436a4b9735ac85d009462ea2e2d6e52f8d7398dd69bb198` |
| `co13` | $Q_{13}$ Coil | `2930` | `Echols2026g` | Sorted transition count profile `[216,220,224,224,226,226,226,226,228,228,228,228,230]` vs `[218,220,222,224,226,226,226,226,228,228,228,228,230]` | `claim/inequiv_co13_2930.txt` | `2,931` | `342cc9c7a9f90b1d336f88ab2a49428d58d676f7b779d59723cdfdcc1d9498db` |
| `sn11` | $Q_{11}$ Snake | `750` | `Echols2026g` | Sorted transition count profile `[65,65,67,68,68,68,69,69,69,71,71]` vs `[65,66,67,68,68,69,69,69,69,70,70]` | `claim/inequiv_sn11_750.txt` | `751` | `78c2a47f837e8e4bcea2a5a69782233ee968e71cb5c7660a0e44f2d2f660b695` |
| `sn12` | $Q_{12}$ Snake | `1480` | `Itty2026a` | Sorted transition count profile `[118,121,122,123,123,123,123,124,125,125,126,127]` vs `[119,121,121,123,123,123,124,124,124,125,126,127]` | `claim/inequiv_sn12_1480.txt` | `1,481` | `2d16153c21433d994b8d787fdd360e877fd3737f96e70a4feded6975bacdaa03` |
| `sn13` | $Q_{13}$ Snake | `2946` | `Toner2026a` | Sorted transition count profile `[220,224,224,225,226,227,227,227,228,229,229,229,231]` vs `[218,224,225,225,226,226,227,227,229,229,229,230,231]` | `claim/inequiv_sn13_2946.txt` | `2,947` | `1708be3f455e2bbb75681d98e33aab6b3c533632085db9926974037eb6c41d1d` |

---

## 4. Audit of Trophy Case & Open Pull Requests

1. **`repo/TROPHY_CASE.md`**: Inspected in full (`12` entries total). None of the prior entries (`#1` Golomb rulers, `#2` Littlewood polynomials, `#3` Kissing number, `#4` Grassl binary linear codes, `#5` Radar arrays, `#6` Covering codes, `#7` HP protein folding, `#8` Optimal sorting networks, `#9` Balanced ternary matrices, `#10` Low-autocorrelation binary sequences, `#11` Cross-free grid graphs, `#12` Erdős #757 Sidon sets) involve `snake-coil-in-the-box` or hypercube snakes/coils.
2. **Open Pull Requests (`elder-plinius/V3R1T4S`)**: Inspected all `77` open PRs returned by the GitHub API (`2026-10-14T10:22:43Z`). Zero open PRs target `snake-coil-in-the-box`.

---

## 5. Summary Conclusion

All pre-registered Partial Win criteria (`p1`, `p2`, and `p3`) are satisfied with strict mathematical novelty verified against `minortriad.com/snake`, `Math-AI-Caltech/Snake-in-the-Box`, `williamtoner/SnakeBox`, `tommyet/snakes`, `repo/TROPHY_CASE.md`, and 2024-2026 literature.

pass: true
