context: subagent
context: subagent (fable)
panel_role: novelty
problem_id: covering-designs-record
claim_id: C_45_14_3_b58

# Novelty Verification Report: Plain Covering Design `C(45, 14, 3)` at `b = 58` Blocks

## 1. Executive Verdict

- **Claimed Record**: Explicit `(45, 14, 3)` plain covering design (`v = 45, k = 14, t = 3, m = 3`) with `b = 58` blocks of size `14` over ground set `{1, ..., 45}` covering all `binom(45, 3) = 14,190` triples, improving the 15-year-old standing world record of `59` blocks by `1` block (`58` is strictly less than `59`, margin `-1` block; Schonheim theoretical lower bound `L(45, 14, 3) = 45`).
- **Certificate Artifacts**: `claim/C_45_14_3_b58.json` and `claim/object/C_45_14_3_b58.json` (`2,807` bytes, SHA-256 `3679cc89320bf75dbc35662d19f4a991ec3f03fb59ee99e0afefe4eee03c95c6`), documented in `claim/CLAIM.md`, `claim/REPRODUCE.md`, `claim/target.md`, and `claim/data/live_tables_snapshot.json`.
- **Novelty Status**: **CONFIRMED STRICT WORLD-RECORD IMPROVEMENT (`58` vs `59`, `-1` block)**.

---

## 2. Live Single-GET Audit of Primary Status Tables

All primary covering design repositories and open pull requests were fetched once via honest single-GET requests (`curl -sS -A "V3R1T4S-novelty-panel/1.0"`):

| Source | URL | Fetch Timestamp (UTC) | HTTP Status | Payload Size (Bytes) | SHA-256 Hash | Standing Entry for `C(45, 14, 3)` |
|---|---|---|---|---|---|---|
| La Jolla Covering Repository (Zenodo `v1.2`, DOI `10.5281/zenodo.10779736`, Record `19735294`) | `https://zenodo.org/api/records/19735294/files/coverdata.json/content` | `2026-10-14T08:02:08Z` | `200` | `8,319,503` | `9e7da3710921066b10234fdc95379a18df3a7d3ae0f8a08ae188ea6bbca92f87` | `size = 59`, `low_bd = 45` (Jan de Heer and Steve Muir, `Private Tools`, `2011-10-11 00:57:02`) |
| La Jolla Covering Repository (GitHub `dmgordo/LJCR`, 2022 dump) | `https://raw.githubusercontent.com/dmgordo/LJCR/main/coverings/coverdata.json` | `2026-10-14T08:03:29Z` | `200` | `6,517,686` | `0984bb8b4c89fe07268569b9814794e3c8852302d075f0794140f202e83d7fef` | `size = 59`, `low_bd = 45` (Jan de Heer and Steve Muir, `Private Tools`, `2011-10-11 00:57:02`) |
| CoveringRepository.com Live Master Table | `https://coveringrepository.com/systems.aspx` | `2026-10-14T08:03:31Z` | `200` | `807,725` | `d5938e025a0a05104878d7ee80a9c0dd04e67e8755cc91407253c804415a6739` | `b = 59`, `sch = 45` (Creator: Jan de Heer and Steve Muir, Method: `Private Tools`, Date: `11/10/2011`) |
| `thebrockchain/covering-designs` GitHub Repository (Falfas 2026) | `https://raw.githubusercontent.com/thebrockchain/covering-designs/main/README.md` | `2026-10-14T08:03:33Z` | `200` | `6,127` | `171f9f5e88341cc90576de0f3016d0ed67569c54e33c1ed16ae729d49b066da5` | No entry for `C(45, 14, 3)` (only `C(28, 13, 4)` at `53` and `C(32, 13, 4)` at `95`) |
| `elder-plinius/V3R1T4S` Open Pull Requests | `https://api.github.com/repos/elder-plinius/V3R1T4S/pulls?state=open&per_page=100` | `2026-10-14T08:03:33Z` | `200` | `1,160,727` | `4757860728d1d16842fbd1772a403c1947b9499bc69b648a1b94feb027d6e5de` | `60` open PRs; `0` PRs on `covering-designs-record` or `C(45, 14, 3)` |

### Exact Historical Improvement Chain in Zenodo LJCR `v1.2` (`coverdata.json`)

The extracted JSON dictionary entry for `"C(45,14,3)"` in Zenodo record `19735294` (`9,482` entries total) lists the complete historical progression prior to this claim:
1. `b = 67`: `LJCR`, `Dynamic programming construction` (`2009-01-11 17:39:13`)
2. `b = 61`: `LJCR`, `Dynamic programming construction` (`2009-01-20 20:02:47`)
3. `b = 60`: `Jan de Heer and Steve Muir`, `Private tools` (`2010-11-11 12:45:21`)
4. `b = 59`: `Jan de Heer and Steve Muir`, `Private Tools` (`2011-10-11 00:57:02`) — **standing world record since October 2011**

---

## 3. Audit of `repo/TROPHY_CASE.md` and Recent Literature (2024–2026)

1. **`repo/TROPHY_CASE.md` Audit**:
   - Contains `53` verified records across `6` problem families (`fmm-small-open-cases`, `erdos850-prime-radicals`, `graph-650-subgraph-isomorphism`, `cap-set-small-dimensions`, `sidon-sets-hadamard`, and `degree-diameter-table`).
   - Contains zero (`0`) entries for `covering-designs-record` or `C(45, 14, 3)`.
2. **2024–2026 Literature & Preprint Audit**:
   - Web and preprint searches across arXiv, Zenodo, and GitHub (`"C(45,14,3)"`, `"C(45, 14, 3)"`, covering design repositories 2024–2026, Gordon LJCR updates, Falfas 2026 `thebrockchain/covering-designs`) confirm that no published paper, preprint, or public dataset reports a `(45, 14, 3)` covering design with fewer than `59` blocks.
   - The claimed `58`-block design strictly beats the standing record of `59` blocks (`58` is strictly less than `59`) and remains strictly above the Schonheim lower bound (`45`).

---

## 4. Novelty Gate Conclusion

The `58`-block plain covering design in `claim/C_45_14_3_b58.json` (`claim/object/C_45_14_3_b58.json`) strictly improves upon the best known bound `C(45, 14, 3) = 59` across all live covering repositories (`coveringrepository.com`, Zenodo LJCR `v1.2`, and GitHub `dmgordo/LJCR`), has no prior entry in `repo/TROPHY_CASE.md` or open pull requests, and is unpublished in the 2024–2026 literature.

pass: true
