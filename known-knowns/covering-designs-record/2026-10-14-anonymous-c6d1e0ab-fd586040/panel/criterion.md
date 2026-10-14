# CRITERION Skeptic Report: `covering-designs-record` — `C(38, 16, 3)` at most `25`

context: subagent
confirmed_scope: Verified that claim/C_38_16_3_b25.json (1,412 bytes, SHA-256 fd58604086de7221e9e4ccea5e65d1475e75fc6e34d0efd50edff09080eb9643) defines a valid plain covering design for C(38, 16, 3) with b = 25 blocks of size 16 over {1, ..., 38} that covers all C(38, 3) = 8,436 3-element subsets, strictly improving by 1 block upon the standing best known upper bound of 26 blocks on both live coveringrepository.com and the La Jolla Covering Repository Zenodo v1.2 archive (and 27 in the dmgordo/LJCR GitHub snapshot).

## 1. Clause-by-Clause Verification Against `claim/target.md`

### 1.1 Victory Condition & Qualifying Tiers
- **Target definition**: A plain covering design ($m = t$) for parameters $(v, k, t)$ is a family $\mathcal{B} = \{B_1, \dots, B_b\}$ of $k$-element subsets (blocks) of $V = \{1, \dots, v\}$ such that every $t$-element subset $T \subseteq V$ is contained in at least one block $B_i \in \mathcal{B}$, establishing $C(v, k, t) \le b$.
- **Claimed result**: Plain covering design ($m = t = 3$) for $(v, k, t) = (38, 16, 3)$ with $b = 25$ blocks, establishing $C(38, 16, 3) \le 25$.
- **Standing record check**:
  - **Primary Live Authority (`coveringrepository.com/systems.aspx` with $m = t = 3$)**: Lists $C(38, 16, 3) \le 26$ (constructed by Franco Atzeni on `27/06/2024`, Schönheim lower bound `19`; raw table SHA-256 `0cf7adf53f60b57da43d0f978bf180d9f704c50913ef184fbd68380d9996fb91`). Beaten by $26 - 25 = 1$ block.
  - **Archival Authority (`10.5281/zenodo.10779736`, Record `19735294`, Version `v1.2`, `coverdata.json`)**: Lists `"v":38,"k":16,"t":3,"size":26,"low_bd":22` (SHA-256 `9e7da3710921066b10234fdc95379a18df3a7d3ae0f8a08ae188ea6bbca92f87`). Beaten by $1$ block.
  - **GitHub Source (`github.com/dmgordo/LJCR`, `coverings/coverdata.json`)**: Lists `"v":38,"k":16,"t":3,"size":27` (SHA-256 `0984bb8b4c89fe07268569b9814794e3c8852302d075f0794140f202e83d7fef`). Beaten by $2$ blocks.
  - **Secondary Authorities (`dmgordon.org/covering-designs/`, `thebrockchain/covering-designs`, arXiv / GitHub literature, `TROPHY_CASE.md`, open PRs)**: None reports any bound strictly below $26$ for $(38, 16, 3)$.
- **Tier classification**: **Full Win** — explicit $(38, 16, 3)$ covering design with $b = 25$ blocks, strictly smaller than the best known upper bound across both `coveringrepository.com` and the La Jolla Covering Repository (`v1.2` Zenodo archive and `dmgordo/LJCR` GitHub).

### 1.2 Independent Re-Execution of `claim/verify_covering.py`
Running `python3 verify_covering.py C_38_16_3_b25.json` in the claim directory produced:
- `File`: `C_38_16_3_b25.json` (`1,412` bytes, SHA-256 `fd58604086de7221e9e4ccea5e65d1475e75fc6e34d0efd50edff09080eb9643`)
- `Parameters`: `v=38, k=16, t=3`
- `Number of blocks`: `b = 25` (`25` distinct blocks)
- `Schönheim lower bound`: `L(38, 16, 3) = 19` (`b = 25` is at least `19`, and at least Zenodo `low_bd = 22`)
- `3-subsets covered`: `8,436 / 8,436` (`100.000000%`, uncovered = `0`)
- `Result`: `VALID C(38, 16, 3) at most 25 covering design.`

### 1.3 Anti-Reward-Hacking Audit (`claim/target.md`)
1. **Complete subset coverage**: Verified by exhaustive $\binom{38}{3} = 8,436$ bitmask check in `claim/verify_covering.py`; zero uncovered $3$-subsets remain.
2. **Exact parameter compliance**: Every one of the $25$ blocks is a list of exactly $16$ strictly increasing integers in $\{1, \dots, 38\}$.
3. **Schönheim sanity bound**:
   $$L(38, 16, 3) = \left\lceil \frac{38}{16} \left\lceil \frac{37}{15} \left\lceil \frac{36}{14} \right\rceil \right\rceil \right\rceil = \left\lceil \frac{38}{16} \left\lceil \frac{37}{15} \cdot 3 \right\rceil \right\rceil = \left\lceil \frac{38}{16} \cdot 8 \right\rceil = 19.$$
   $b = 25 \ge 19$ (and $25 \ge 22$).
4. **Live table cross-check**: Both `coveringrepository.com` ($26$, Franco Atzeni 2024) and Zenodo `10.5281/zenodo.10779736` `v1.2` ($26$) were checked; $b = 25$ strictly beats the minimum of all live and archival bounds ($\min(26, 26, 27) = 26$).
5. **Plain covering vs. Turán covering**: Verified $m = t = 3$ (every $3$-subset is contained in at least one $16$-block).
6. **Table scope and verification feasibility**: $v = 38 \le 99$, $k = 16 \le 25$, $t = 3 \le 8$, and $\binom{38}{3} = 8,436 \le 5 \times 10^9$.

### 1.4 Required Deliverables Audit
- `claim/C_38_16_3_b25.json`: Present, self-contained JSON with `v`, `k`, `t`, `b`, `previous_best`, `source_beaten`, and `blocks`.
- `claim/verify_covering.py`: Present, standalone Python 3 standard-library verifier checking block count, block size, element range, element distinctness, Schönheim bound, and full $\binom{v}{t}$ coverage.
- `claim/CLAIM.md` and `claim/REPRODUCE.md`: Complete, self-consistent, and accurately document the standing record and verification command.

## 2. Verdict
All scope, anti-reward-hacking, and deliverable requirements in `claim/target.md` are fully satisfied.

pass: true
