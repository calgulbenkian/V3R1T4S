context: subagent
context: subagent (fable)
panel_role: novelty
problem_id: covering-designs-record
claim_id: C_55_14_3_b97

# Novelty Verification Report: Plain Covering Design `C(55, 14, 3)` at `b = 97` Blocks

## 1. Executive Verdict

- **Claimed Record**: Explicit `(55, 14, 3)` plain covering design (`v = 55, k = 14, t = 3, m = 3`) with `b = 97` blocks of size `14` over ground set `{1, ..., 55}` covering all `binom(55, 3) = 26,235` triples, improving the standing world record of `99` blocks by `2` blocks (`97` is strictly less than `99`, margin `-2` blocks; Schonheim theoretical lower bound `L(55, 14, 3) = 83`).
- **Certificate Artifacts**: `claim/C_55_14_3_b97.json` and `claim/object/C_55_14_3_b97.json` (`4,653` bytes, SHA-256 `8b401301e40d62ee5d6b1b91d4ce4659e9f1c0489404de6515d090ae6f6ecacb`), documented in `claim/CLAIM.md`, `claim/REPRODUCE.md`, `claim/target.md`, and `claim/data/live_tables_snapshot.json`.
- **Novelty Status**: **CONFIRMED STRICT WORLD-RECORD IMPROVEMENT (`97` vs `99`, `-2` blocks)**.

---

## 2. Live Single-GET Audit of Primary Status Tables

All primary covering design repositories and open pull requests were fetched once via honest single-GET requests (`curl -sS -A "V3R1T4S-novelty-panel/1.0"`):

| Source | URL | Fetch Timestamp (UTC) | HTTP Status | Payload Size (Bytes) | SHA-256 Hash | Standing Entry for `C(55, 14, 3)` |
|---|---|---|---|---|---|---|
| La Jolla Covering Repository (Zenodo `v1.2`, DOI `10.5281/zenodo.10779736`, Record `19735294`) | `https://zenodo.org/api/records/19735294/files/coverdata.json/content` | `2026-10-14T08:02:08Z` | `200` | `8,319,503` | `9e7da3710921066b10234fdc95379a18df3a7d3ae0f8a08ae188ea6bbca92f87` | `size = 99`, `low_bd = 83` (Franco Atzeni, `local search`, `2024-08-03 10:48:51`) |
| La Jolla Covering Repository (GitHub `dmgordo/LJCR`, 2022 dump) | `https://raw.githubusercontent.com/dmgordo/LJCR/main/coverings/coverdata.json` | `2026-10-14T08:03:29Z` | `200` | `6,517,686` | `0984bb8b4c89fe07268569b9814794e3c8852302d075f0794140f202e83d7fef` | `size = 101`, `low_bd = 83` (Jan de Heer and Steve Muir, `Private tools`, `2013-09-05 10:22:11`) |
| CoveringRepository.com Live Master Table | `https://coveringrepository.com/systems.aspx` | `2026-10-14T08:03:31Z` | `200` | `807,725` | `d5938e025a0a05104878d7ee80a9c0dd04e67e8755cc91407253c804415a6739` | `b = 99`, `sch = 83` (Creator: Franco Atzeni, Method: `local search`, Date: `03/08/2024`) |
| `thebrockchain/covering-designs` GitHub Repository (Falfas 2026) | `https://raw.githubusercontent.com/thebrockchain/covering-designs/main/README.md` | `2026-10-14T08:03:33Z` | `200` | `6,127` | `171f9f5e88341cc90576de0f3016d0ed67569c54e33c1ed16ae729d49b066da5` | No entry for `C(55, 14, 3)` (only `C(28, 13, 4)` at `53` and `C(32, 13, 4)` at `95`) |
| `elder-plinius/V3R1T4S` Open Pull Requests | `https://api.github.com/repos/elder-plinius/V3R1T4S/pulls?state=open&per_page=100` | `2026-10-14T08:03:33Z` | `200` | `1,160,727` | `4757860728d1d16842fbd1772a403c1947b9499bc69b648a1b94feb027d6e5de` | `60` open PRs; `0` PRs on `covering-designs-record` or `C(55, 14, 3)` |

### Exact Historical Improvement Chain in Zenodo LJCR `v1.2` (`coverdata.json`)

The extracted JSON dictionary entry for `"C(55,14,3)"` in Zenodo record `19735294` (`9,482` entries total) lists the complete historical progression prior to this claim:
1. `b = 122`: `LJCR`, `Simple construction from (56,14,3)` (`2009-01-10 10:07:30`)
2. `b = 121`: `Michael Dambmann`, `Simulated Annealing` (`2009-01-18 05:02:23`) / `LJCR` (`2009-08-10 14:10:20`)
3. `b = 120`: `LJCR`, `Simple construction from (56,14,3)` (`2009-08-14 07:58:38`)
4. `b = 102`: `Jan de Heer and Steve Muir`, `Private Tools` (`2011-10-11 00:58:35`)
5. `b = 101`: `Jan de Heer and Steve Muir`, `Private tools` (`2013-09-05 10:22:11`)
6. `b = 100`: `Alessandro Jurcovich` (`2023-02-10 01:40:14`)
7. `b = 99`: `Franco Atzeni`, `local search` (`2024-08-03 10:48:51`) — **standing world record**

---

## 3. Audit of `repo/TROPHY_CASE.md` and Recent Literature (2024–2026)

1. **`repo/TROPHY_CASE.md` Audit**:
   - Contains `53` verified records across `6` problem families (`fmm-small-open-cases`, `erdos850-prime-radicals`, `graph-650-subgraph-isomorphism`, `cap-set-small-dimensions`, `sidon-sets-hadamard`, and `degree-diameter-table`).
   - Contains zero (`0`) entries for `covering-designs-record` or `C(55, 14, 3)`.
2. **2024–2026 Literature & Preprint Audit**:
   - Web and preprint searches across arXiv, Zenodo, and GitHub (`"C(55,14,3)"`, `"C(55, 14, 3)"`, covering design repositories 2024–2026, Gordon LJCR updates, Falfas 2026 `thebrockchain/covering-designs`) confirm that no published paper, preprint, or public dataset reports a `(55, 14, 3)` covering design with fewer than `99` blocks.
   - The claimed `97`-block design strictly beats the standing record of `99` blocks by `2` blocks (`97` is strictly less than `99`) and remains strictly above the Schonheim lower bound (`83`).

---

## 4. Novelty Gate Conclusion

The `97`-block plain covering design in `claim/C_55_14_3_b97.json` (`claim/object/C_55_14_3_b97.json`) strictly improves upon the best known bound `C(55, 14, 3) = 99` across all live covering repositories (`coveringrepository.com`, Zenodo LJCR `v1.2`, and GitHub `dmgordo/LJCR`), has no prior entry in `repo/TROPHY_CASE.md` or open pull requests, and is unpublished in the 2024–2026 literature.

pass: true
