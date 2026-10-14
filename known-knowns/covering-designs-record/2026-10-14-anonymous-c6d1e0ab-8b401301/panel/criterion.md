# CRITERION Skeptic Report: `covering-designs-record` — `C(55, 14, 3)` at most `97`

context: subagent
confirmed_scope: Verified that claim/C_55_14_3_b97.json (4,653 bytes, SHA-256 8b401301e40d62ee5d6b1b91d4ce4659e9f1c0489404de6515d090ae6f6ecacb) defines a valid plain covering design for C(55, 14, 3) with b = 97 blocks of size 14 over {1, ..., 55} that covers all C(55, 3) = 26,235 3-element subsets, strictly improving by 2 blocks upon the standing best known upper bound of 99 blocks on both live coveringrepository.com and the La Jolla Covering Repository Zenodo v1.2 archive (and 101 in the dmgordo/LJCR GitHub snapshot).

## 1. Clause-by-Clause Verification Against `claim/target.md`

### 1.1 Victory Condition & Qualifying Tiers
- **Target definition**: A plain covering design ($m = t$) for parameters $(v, k, t)$ is a family $\mathcal{B} = \{B_1, \dots, B_b\}$ of $k$-element subsets (blocks) of $V = \{1, \dots, v\}$ such that every $t$-element subset $T \subseteq V$ is contained in at least one block $B_i \in \mathcal{B}$, establishing $C(v, k, t) \le b$.
- **Claimed result**: Plain covering design ($m = t = 3$) for $(v, k, t) = (55, 14, 3)$ with $b = 97$ blocks, establishing $C(55, 14, 3) \le 97$.
- **Standing record check**:
  - **Primary Live Authority (`coveringrepository.com/systems.aspx` with $m = t = 3$)**: Lists $C(55, 14, 3) \le 99$ (constructed by Franco Atzeni on `03/08/2024`, Schönheim lower bound `83`; raw table SHA-256 `0cf7adf53f60b57da43d0f978bf180d9f704c50913ef184fbd68380d9996fb91`). Beaten by $99 - 97 = 2$ blocks.
  - **Archival Authority (`10.5281/zenodo.10779736`, Record `19735294`, Version `v1.2`, `coverdata.json`)**: Lists `"v":55,"k":14,"t":3,"size":99,"low_bd":83` (SHA-256 `9e7da3710921066b10234fdc95379a18df3a7d3ae0f8a08ae188ea6bbca92f87`). Beaten by $2$ blocks.
  - **GitHub Source (`github.com/dmgordo/LJCR`, `coverings/coverdata.json`)**: Lists `"v":55,"k":14,"t":3,"size":101` (SHA-256 `0984bb8b4c89fe07268569b9814794e3c8852302d075f0794140f202e83d7fef`). Beaten by $4$ blocks.
  - **Secondary Authorities (`dmgordon.org/covering-designs/`, `thebrockchain/covering-designs`, arXiv / GitHub literature, `TROPHY_CASE.md`, open PRs)**: None reports any bound strictly below $99$ for $(55, 14, 3)$.
- **Tier classification**: **Full Win** — explicit $(55, 14, 3)$ covering design with $b = 97$ blocks, strictly smaller than the best known upper bound across both `coveringrepository.com` and the La Jolla Covering Repository (`v1.2` Zenodo archive and `dmgordo/LJCR` GitHub).

### 1.2 Independent Re-Execution of `claim/verify_covering.py`
Running `python3 verify_covering.py C_55_14_3_b97.json` in the claim directory produced:
- `File`: `C_55_14_3_b97.json` (`4,653` bytes, SHA-256 `8b401301e40d62ee5d6b1b91d4ce4659e9f1c0489404de6515d090ae6f6ecacb`)
- `Parameters`: `v=55, k=14, t=3`
- `Number of blocks`: `b = 97` (`97` distinct blocks)
- `Schönheim lower bound`: `L(55, 14, 3) = 83` (`b = 97` is at least `83`)
- `3-subsets covered`: `26,235 / 26,235` (`100.000000%`, uncovered = `0`)
- `Result`: `VALID C(55, 14, 3) at most 97 covering design.`

### 1.3 Anti-Reward-Hacking Audit (`claim/target.md`)
1. **Complete subset coverage**: Verified by exhaustive $\binom{55}{3} = 26,235$ bitmask check in `claim/verify_covering.py`; zero uncovered $3$-subsets remain.
2. **Exact parameter compliance**: Every one of the $97$ blocks is a list of exactly $14$ strictly increasing integers in $\{1, \dots, 55\}$.
3. **Schönheim sanity bound**:
   $$L(55, 14, 3) = \left\lceil \frac{55}{14} \left\lceil \frac{54}{13} \left\lceil \frac{53}{12} \right\rceil \right\rceil \right\rceil = \left\lceil \frac{55}{14} \left\lceil \frac{54}{13} \cdot 5 \right\rceil \right\rceil = \left\lceil \frac{55}{14} \cdot 21 \right\rceil = 83.$$
   $b = 97 \ge 83$.
4. **Live table cross-check**: Both `coveringrepository.com` ($99$, Franco Atzeni 2024) and Zenodo `10.5281/zenodo.10779736` `v1.2` ($99$) were checked; $b = 97$ strictly beats the minimum of all live and archival bounds ($\min(99, 99, 101) = 99$).
5. **Plain covering vs. Turán covering**: Verified $m = t = 3$ (every $3$-subset is contained in at least one $14$-block).
6. **Table scope and verification feasibility**: $v = 55 \le 99$, $k = 14 \le 25$, $t = 3 \le 8$, and $\binom{55}{3} = 26,235 \le 5 \times 10^9$.

### 1.4 Required Deliverables Audit
- `claim/C_55_14_3_b97.json`: Present, self-contained JSON with `v`, `k`, `t`, `b`, `previous_best`, `source_beaten`, and `blocks`.
- `claim/verify_covering.py`: Present, standalone Python 3 standard-library verifier checking block count, block size, element range, element distinctness, Schönheim bound, and full $\binom{v}{t}$ coverage.
- `claim/CLAIM.md` and `claim/REPRODUCE.md`: Complete, self-consistent, and accurately document the standing record and verification command.

## 2. Verdict
All scope, anti-reward-hacking, and deliverable requirements in `claim/target.md` are fully satisfied.

pass: true
