# CRITERION Skeptic Report: `covering-designs-record` — `C(45, 14, 3)` at most `58`

context: subagent
confirmed_scope: Verified that claim/C_45_14_3_b58.json (2,807 bytes, SHA-256 3679cc89320bf75dbc35662d19f4a991ec3f03fb59ee99e0afefe4eee03c95c6) defines a valid plain covering design for C(45, 14, 3) with b = 58 blocks of size 14 over {1, ..., 45} that covers all C(45, 3) = 14,190 3-element subsets, strictly improving by 1 block upon the standing best known upper bound of 59 blocks on both live coveringrepository.com and the La Jolla Covering Repository Zenodo v1.2 archive (and 59 in the dmgordo/LJCR GitHub snapshot).

## 1. Clause-by-Clause Verification Against `claim/target.md`

### 1.1 Victory Condition & Qualifying Tiers
- **Target definition**: A plain covering design ($m = t$) for parameters $(v, k, t)$ is a family $\mathcal{B} = \{B_1, \dots, B_b\}$ of $k$-element subsets (blocks) of $V = \{1, \dots, v\}$ such that every $t$-element subset $T \subseteq V$ is contained in at least one block $B_i \in \mathcal{B}$, establishing $C(v, k, t) \le b$.
- **Claimed result**: Plain covering design ($m = t = 3$) for $(v, k, t) = (45, 14, 3)$ with $b = 58$ blocks, establishing $C(45, 14, 3) \le 58$.
- **Standing record check**:
  - **Primary Live Authority (`coveringrepository.com/systems.aspx` with $m = t = 3$)**: Lists $C(45, 14, 3) \le 59$ (constructed by Jan de Heer and Steve Muir on `11/10/2011`, Schönheim lower bound `45`; raw table SHA-256 `0cf7adf53f60b57da43d0f978bf180d9f704c50913ef184fbd68380d9996fb91`). Beaten by $59 - 58 = 1$ block.
  - **Archival Authority (`10.5281/zenodo.10779736`, Record `19735294`, Version `v1.2`, `coverdata.json`)**: Lists `"v":45,"k":14,"t":3,"size":59,"low_bd":45` (SHA-256 `9e7da3710921066b10234fdc95379a18df3a7d3ae0f8a08ae188ea6bbca92f87`). Beaten by $1$ block.
  - **GitHub Source (`github.com/dmgordo/LJCR`, `coverings/coverdata.json`)**: Lists `"v":45,"k":14,"t":3,"size":59` (SHA-256 `0984bb8b4c89fe07268569b9814794e3c8852302d075f0794140f202e83d7fef`). Beaten by $1$ block.
  - **Secondary Authorities (`dmgordon.org/covering-designs/`, `thebrockchain/covering-designs`, arXiv / GitHub literature, `TROPHY_CASE.md`, open PRs)**: None reports any bound strictly below $59$ for $(45, 14, 3)$.
- **Tier classification**: **Full Win** — explicit $(45, 14, 3)$ covering design with $b = 58$ blocks, strictly smaller than the best known upper bound across both `coveringrepository.com` and the La Jolla Covering Repository (`v1.2` Zenodo archive and `dmgordo/LJCR` GitHub).

### 1.2 Independent Re-Execution of `claim/verify_covering.py`
Running `python3 verify_covering.py C_45_14_3_b58.json` in the claim directory produced:
- `File`: `C_45_14_3_b58.json` (`2,807` bytes, SHA-256 `3679cc89320bf75dbc35662d19f4a991ec3f03fb59ee99e0afefe4eee03c95c6`)
- `Parameters`: `v=45, k=14, t=3`
- `Number of blocks`: `b = 58` (`58` distinct blocks)
- `Schönheim lower bound`: `L(45, 14, 3) = 45` (`b = 58` is at least `45`)
- `3-subsets covered`: `14,190 / 14,190` (`100.000000%`, uncovered = `0`)
- `Result`: `VALID C(45, 14, 3) at most 58 covering design.`

### 1.3 Anti-Reward-Hacking Audit (`claim/target.md`)
1. **Complete subset coverage**: Verified by exhaustive $\binom{45}{3} = 14,190$ bitmask check in `claim/verify_covering.py`; zero uncovered $3$-subsets remain.
2. **Exact parameter compliance**: Every one of the $58$ blocks is a list of exactly $14$ strictly increasing integers in $\{1, \dots, 45\}$.
3. **Schönheim sanity bound**:
   $$L(45, 14, 3) = \left\lceil \frac{45}{14} \left\lceil \frac{44}{13} \left\lceil \frac{43}{12} \right\rceil \right\rceil \right\rceil = \left\lceil \frac{45}{14} \left\lceil \frac{44}{13} \cdot 4 \right\rceil \right\rceil = \left\lceil \frac{45}{14} \cdot 14 \right\rceil = 45.$$
   $b = 58 \ge 45$.
4. **Live table cross-check**: Both `coveringrepository.com` ($59$, Jan de Heer and Steve Muir 2011) and Zenodo `10.5281/zenodo.10779736` `v1.2` ($59$) were checked; $b = 58$ strictly beats the minimum of all live and archival bounds ($\min(59, 59, 59) = 59$).
5. **Plain covering vs. Turán covering**: Verified $m = t = 3$ (every $3$-subset is contained in at least one $14$-block).
6. **Table scope and verification feasibility**: $v = 45 \le 99$, $k = 14 \le 25$, $t = 3 \le 8$, and $\binom{45}{3} = 14,190 \le 5 \times 10^9$.

### 1.4 Required Deliverables Audit
- `claim/C_45_14_3_b58.json`: Present, self-contained JSON with `v`, `k`, `t`, `b`, `previous_best`, `source_beaten`, and `blocks`.
- `claim/verify_covering.py`: Present, standalone Python 3 standard-library verifier checking block count, block size, element range, element distinctness, Schönheim bound, and full $\binom{v}{t}$ coverage.
- `claim/CLAIM.md` and `claim/REPRODUCE.md`: Complete, self-consistent, and accurately document the standing record and verification command.

## 2. Verdict
All scope, anti-reward-hacking, and deliverable requirements in `claim/target.md` are fully satisfied.

pass: true
