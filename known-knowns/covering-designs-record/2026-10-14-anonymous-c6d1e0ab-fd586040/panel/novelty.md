context: subagent
context: subagent (fable)
panel_role: novelty
problem_id: covering-designs-record
claim_id: C_38_16_3_b25

# Novelty Verification Report: Plain Covering Design `C(38, 16, 3)` at `b = 25` Blocks

## 1. Executive Verdict

- **Claimed Record**: Explicit `(38, 16, 3)` plain covering design (`v = 38, k = 16, t = 3, m = 3`) with `b = 25` blocks of size `16` over ground set `{1, ..., 38}` covering all `binom(38, 3) = 8,436` triples, improving the standing world record of `26` blocks by `1` block (`25` is strictly less than `26`, margin `-1` block; Schonheim theoretical lower bound `L(38, 16, 3) = 19` and LJCR refined lower bound `low_bd = 22`).
- **Certificate Artifacts**: `claim/C_38_16_3_b25.json` and `claim/object/C_38_16_3_b25.json` (`1,412` bytes, SHA-256 `fd58604086de7221e9e4ccea5e65d1475e75fc6e34d0efd50edff09080eb9643`), documented in `claim/CLAIM.md`, `claim/REPRODUCE.md`, `claim/target.md`, and `claim/data/live_tables_snapshot.json`.
- **Novelty Status**: **CONFIRMED STRICT WORLD-RECORD IMPROVEMENT (`25` vs `26`, `-1` block)**.

---

## 2. Live Single-GET Audit of Primary Status Tables

All primary covering design repositories and open pull requests were fetched once via honest single-GET requests (`curl -sS -A "V3R1T4S-novelty-panel/1.0"`):

| Source | URL | Fetch Timestamp (UTC) | HTTP Status | Payload Size (Bytes) | SHA-256 Hash | Standing Entry for `C(38, 16, 3)` |
|---|---|---|---|---|---|---|
| La Jolla Covering Repository (Zenodo `v1.2`, DOI `10.5281/zenodo.10779736`, Record `19735294`) | `https://zenodo.org/api/records/19735294/files/coverdata.json/content` | `2026-10-14T08:02:08Z` | `200` | `8,319,503` | `9e7da3710921066b10234fdc95379a18df3a7d3ae0f8a08ae188ea6bbca92f87` | `size = 26`, `low_bd = 22` (Franco Atzeni, `local search`, `2024-06-27 12:03:22`) |
| La Jolla Covering Repository (GitHub `dmgordo/LJCR`, 2022 dump) | `https://raw.githubusercontent.com/dmgordo/LJCR/main/coverings/coverdata.json` | `2026-10-14T08:03:29Z` | `200` | `6,517,686` | `0984bb8b4c89fe07268569b9814794e3c8852302d075f0794140f202e83d7fef` | `size = 27`, `low_bd = 22` (LJCR, `Multiple of (19,8,3) covering`, `2009-01-21 19:44:56`) |
| CoveringRepository.com Live Master Table | `https://coveringrepository.com/systems.aspx` | `2026-10-14T08:03:31Z` | `200` | `807,725` | `d5938e025a0a05104878d7ee80a9c0dd04e67e8755cc91407253c804415a6739` | `b = 26`, `sch = 22` (Creator: Franco Atzeni, Method: `local search`, Date: `27/06/2024`) |
| `thebrockchain/covering-designs` GitHub Repository (Falfas 2026) | `https://raw.githubusercontent.com/thebrockchain/covering-designs/main/README.md` | `2026-10-14T08:03:33Z` | `200` | `6,127` | `171f9f5e88341cc90576de0f3016d0ed67569c54e33c1ed16ae729d49b066da5` | No entry for `C(38, 16, 3)` (only `C(28, 13, 4)` at `53` and `C(32, 13, 4)` at `95`) |
| `elder-plinius/V3R1T4S` Open Pull Requests | `https://api.github.com/repos/elder-plinius/V3R1T4S/pulls?state=open&per_page=100` | `2026-10-14T08:03:33Z` | `200` | `1,160,727` | `4757860728d1d16842fbd1772a403c1947b9499bc69b648a1b94feb027d6e5de` | `60` open PRs; `0` PRs on `covering-designs-record` or `C(38, 16, 3)` |

### Exact Historical Improvement Chain in Zenodo LJCR `v1.2` (`coverdata.json`)

The extracted JSON dictionary entry for `"C(38,16,3)"` in Zenodo record `19735294` (`9,482` entries total) lists the complete historical progression prior to this claim:
1. `b = 44`: `LJCR`, `Simple construction from (38,15,3)` (`2009-01-08 19:25:14`)
2. `b = 34`: `LJCR`, `Simple construction from (38,15,3)` (`2009-01-10 10:04:26`)
3. `b = 30`: `LJCR`, `Simple construction from (39,16,3)` (`2009-01-10 18:31:32`)
4. `b = 28`: `LJCR`, `Simple construction from (39,16,3)` (`2009-01-20 19:50:33`)
5. `b = 27`: `LJCR`, `Multiple of (19,8,3) covering` (`2009-01-21 19:44:56`)
6. `b = 26`: `Franco Atzeni`, `local search` (`2024-06-27 12:03:22`) — **standing world record**

---

## 3. Audit of `repo/TROPHY_CASE.md` and Recent Literature (2024–2026)

1. **`repo/TROPHY_CASE.md` Audit**:
   - Contains `53` verified records across `6` problem families (`fmm-small-open-cases`, `erdos850-prime-radicals`, `graph-650-subgraph-isomorphism`, `cap-set-small-dimensions`, `sidon-sets-hadamard`, and `degree-diameter-table`).
   - Contains zero (`0`) entries for `covering-designs-record` or `C(38, 16, 3)`.
2. **2024–2026 Literature & Preprint Audit**:
   - Web and preprint searches across arXiv, Zenodo, and GitHub (`"C(38,16,3)"`, `"C(38, 16, 3)"`, covering design repositories 2024–2026, Gordon LJCR updates, Falfas 2026 `thebrockchain/covering-designs`) confirm that no published paper, preprint, or public dataset reports a `(38, 16, 3)` covering design with fewer than `26` blocks.
   - The claimed `25`-block design strictly beats the standing record of `26` blocks (`25` is strictly less than `26`) and remains strictly above the Schonheim (`19`) and LJCR (`22`) lower bounds.

---

## 4. Novelty Gate Conclusion

The `25`-block plain covering design in `claim/C_38_16_3_b25.json` (`claim/object/C_38_16_3_b25.json`) strictly improves upon the best known bound `C(38, 16, 3) = 26` across all live covering repositories (`coveringrepository.com`, Zenodo LJCR `v1.2`, and GitHub `dmgordo/LJCR`), has no prior entry in `repo/TROPHY_CASE.md` or open pull requests, and is unpublished in the 2024–2026 literature.

pass: true
