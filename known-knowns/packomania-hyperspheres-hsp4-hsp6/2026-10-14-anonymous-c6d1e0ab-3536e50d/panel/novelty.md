context: subagent
context: subagent (fable)
panel_role: novelty_skeptic
run_id: 2026-10-14-1020
problem_id: packomania-hyperspheres-hsp4-hsp6
claim_type: solution_claim (Full Win at d=4, N=170 + Partial Wins p2, p3)
audit_timestamp_utc: 2026-10-14T12:01:00Z

# NOVELTY SKEPTIC AUDIT REPORT: Packomania 4D Hypersphere Packing Record at N = 170 (Full Win + Partial Wins p2, p3)

## 1. Executive Verdict

I have audited the Full Win (`solution_claim`) and Partial Wins (`p2`, `p3`) in `claim/CLAIM.md`, `claim/REPRODUCE.md`, `claim/VERDICT.md`, `claim/target.md`, `claim/verify_hsp.py`, `claim/WIN_hsp4_170_polished.txt`, `claim/WIN_transplant_hsp4_170.txt`, `claim/EXT_hsp4_301.txt`, `claim/EXT_hsp4_301_baseline.txt`, and `claim/audit_report.txt` against:
1. Fresh single-GET live fetches (`curl -sS -L -A "V3R1T4S-novelty-panel/1.0"`) of all primary Packomania sources at `2026-10-14T12:00:15Z` through `2026-10-14T12:00:18Z`:
   - `https://packomania.com/hsp4/txt/radius.txt` (`2026-10-14T12:00:15Z`, HTTP `200`, `5,575` bytes, SHA-256 `f3ddaa944aac014718bc9f5438700698abedac0189266198df8bb60772ac569f`);
   - `https://packomania.com/hsp4/hsp4.html` (`2026-10-14T12:00:16Z`, HTTP `200`, `88,618` bytes, SHA-256 `1c3a30644ba8ff73955547ff94e769a1983c146f4d2b14989eab3e0060a3feb3`);
   - `https://packomania.com/hsp5/txt/radius.txt` (`2026-10-14T12:00:17Z`, HTTP `200`, `5,575` bytes, SHA-256 `2c87be8ca80d6c74044e2cb4c56acd8d0b735fb70faedc96fd54a1db1be18cf8`);
   - `https://packomania.com/hsp6/txt/radius.txt` (`2026-10-14T12:00:18Z`, HTTP `200`, `4,796` bytes, SHA-256 `7521a740ca4766d4f9f0d9c9b971617d6a315a32e9a050a2b9a0003357750817`);
   - `https://packomania.com/pending-requests.html` (`2026-10-14T12:00:18Z`, HTTP `200`, `4,954` bytes, SHA-256 `0d6ebbbe8e95abe7e701e1c70fbc1c0ec5bb06d611822b0b135ce3b776972384`);
2. A fresh single-GET live fetch of open pull requests on `elder-plinius/V3R1T4S` (`https://api.github.com/repos/elder-plinius/V3R1T4S/pulls?state=open&per_page=100`, `2026-10-14T12:00:19Z`, HTTP `200`, `1,863,557` bytes, SHA-256 `e0bb7b6a3d97856d9e365199d89763b7632ef2131df55c7435c1ddbc2917f2e4`, `100` open PRs returned) and full inspection of `repo/TROPHY_CASE.md`;
3. A 2024-2026 literature search for 4D hypersphere packings inside a unit 4-ball (`hsp4`, `N = 170` and `N = 301`).

All novelty criteria for the **Full Win (`solution_claim`)** and **Partial Wins (`p2`, `p3`)** are unconditionally satisfied:
- **Full Win (`d = 4, N = 170`, `claim/WIN_hsp4_170_polished.txt`)**: The live `hsp4/txt/radius.txt` scoreboard lists `170 0.215589695168` (`Eckard Specht`, table last updated `06-Jul-2025` on `hsp4.html`). Our polished configuration `claim/WIN_hsp4_170_polished.txt` achieves certified 25-digit radius **`r* = 0.2156450594683900081281903`**, strictly beating the live record by **`+0.0000553643003900081281903`** (`+5.536430e-05`, **553,643x** above the required `1e-10` threshold), and is provably non-isometric to the posted `hsp4-170.txt` (`claim/ref_hsp4_170.txt`) with maximum sorted pairwise distance difference **`9.031040e-03`** (**903,104x** above `1e-8`). The initial two-stage core-transplanted certificate `claim/WIN_transplant_hsp4_170.txt` also independently beats the live record at **`r* = 0.2156371457737953995400180`** (`+4.745061e-05`, **474,506x** above `1e-10`).
- **Partial Win `p2` (`d = 4, N = 301` Extension Row, `claim/EXT_hsp4_301.txt`)**: The live `hsp4/txt/radius.txt` table contains `299` rows (`N = 2..300`, ending at `300 0.187648382196`). Our certified extension packing at `N = 301` (`claim/EXT_hsp4_301.txt`) achieves **`r* = 0.1875249820010892044888787`**, strictly beating the single-cavity insertion and re-jamming baseline (`claim/EXT_hsp4_301_baseline.txt`, `r* = 0.1856364718236760681178868`) by **`+0.0018885101774131363709919`** (`+1.888510e-03`).
- **Partial Win `p3` (Full Contact-Graph & Data-Integrity Audit, `claim/audit_report.txt`)**: Audits all `856` listed rows across `hsp4` (`N = 2..300`), `hsp5` (`N = 2..300`), and `hsp6` (`N = 2..259`), uncovering a systemic 4D coordinate truncation bug across all `299` files in `hsp5_coords.tar.gz` and all `249` present files in `hsp6_coords.tar.gz`, plus `9` missing coordinate files (`hsp6-251.txt` through `hsp6-259.txt`) in `hsp6_coords.tar.gz`.
- **Pending-Queue Rule & Caveat Disclosure**: Live `https://packomania.com/pending-requests.html` (`08-Oct-2026`, verified `2026-10-14T12:00:18Z`) contains `0` entries naming `hsp4`, `hsp5`, or `hsp6`. Per `claim/target.md`, we explicitly state the caveat that `pending-requests.html` includes an uncategorized bundle `26-Sep-2026 01:11 Moki & Julio *many* 4666 candidates total` whose target categories are unspecified, so `d = 4, N = 170` should be re-checked against the live table once that bundle is processed.

---

## 2. Live Scoreboard & Pending-Queue Audit (Single-GET Provenance)

All external sources were verified using single-GET requests (`curl -sS -L -A "V3R1T4S-novelty-panel/1.0"`). No retries or automated loops were performed.

| Source | URL | Fetch Timestamp (UTC) | HTTP Status | Bytes | SHA-256 | Extracted Live Cells / Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `hsp4` Radius Table | `https://packomania.com/hsp4/txt/radius.txt` | `2026-10-14T12:00:15Z` | `200` | `5,575` | `f3ddaa944aac014718bc9f5438700698abedac0189266198df8bb60772ac569f` | `299` rows (`N = 2..300`); `169 0.215785895566`, **`170 0.215589695168`**, `171 0.215441346347`, ..., `300 0.187648382196` |
| `hsp4` Overview & History | `https://packomania.com/hsp4/hsp4.html` | `2026-10-14T12:00:16Z` | `200` | `88,618` | `1c3a30644ba8ff73955547ff94e769a1983c146f4d2b14989eab3e0060a3feb3` | `Last update: 06-Jul-2025`; History of updates ends `06-Jul-2025` (E. Specht) |
| `hsp5` Radius Table | `https://packomania.com/hsp5/txt/radius.txt` | `2026-10-14T12:00:17Z` | `200` | `5,575` | `2c87be8ca80d6c74044e2cb4c56acd8d0b735fb70faedc96fd54a1db1be18cf8` | `299` rows (`N = 2..300`); `2 0.500000000000` .. `300 0.234892444467` |
| `hsp6` Radius Table | `https://packomania.com/hsp6/txt/radius.txt` | `2026-10-14T12:00:18Z` | `200` | `4,796` | `7521a740ca4766d4f9f0d9c9b971617d6a315a32e9a050a2b9a0003357750817` | `258` rows (`N = 2..259`); `2 0.500000000000` .. `259 0.275354579268` |
| Packomania Pending Queue | `https://packomania.com/pending-requests.html` | `2026-10-14T12:00:18Z` | `200` | `4,954` | `0d6ebbbe8e95abe7e701e1c70fbc1c0ec5bb06d611822b0b135ce3b776972384` | Dated `08-Oct-2026`; `0` entries naming `hsp4`, `hsp5`, or `hsp6` (categories: `csc`, `ccq`, `crt`, `csq`, `chx`, `cpt`, `crc`, `cxd`, `csqv`, plus `26-Sep-2026 01:11 Moki & Julio *many* 4666 candidates total`) |
| `elder-plinius/V3R1T4S` Open PRs | `https://api.github.com/repos/elder-plinius/V3R1T4S/pulls?state=open&per_page=100` | `2026-10-14T12:00:19Z` | `200` | `1,863,557` | `e0bb7b6a3d97856d9e365199d89763b7632ef2131df55c7435c1ddbc2917f2e4` | `100` open PRs returned; `0` PRs touch `packomania-hyperspheres-hsp4-hsp6` |

---

## 3. Cell-by-Cell Novelty Comparison and Artifact Inventory

| Achievement Type | Target Parameter | Live Packomania Reference | Reference Holder / Source | Claimed Certified Value (`claim/`) | Strict Net Gain (`r* - r_ref`) | Artifact Relative Path | Bytes | SHA-256 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Full Win (`solution_claim`, polished)** | `d = 4, N = 170` | `0.215589695168` | `Eckard Specht` (`hsp4/txt/radius.txt`) | **`0.2156450594683900081281903`** | **`+0.0000553643003900081281903`** (`+5.536430e-05`, **553,643x** above `1e-10`) | `claim/WIN_hsp4_170_polished.txt` | `16,513` | `3536e50dd047d04f09605dabb6bf33b5c17a9bfaf502147c2cc43c9da215bb65` |
| **Full Win (`solution_claim`, initial transplant)** | `d = 4, N = 170` | `0.215589695168` | `Eckard Specht` (`hsp4/txt/radius.txt`) | **`0.2156371457737953995400180`** | **`+0.0000474506057953995400180`** (`+4.745061e-05`, **474,506x** above `1e-10`) | `claim/WIN_transplant_hsp4_170.txt` | `16,513` | `28fc7445979a5f993a5d85ea91c60cfd421f87faff62b74e8121c5bbc9cb5627` |
| **Partial Win (`p2`, extension row)** | `d = 4, N = 301` | `0.1856364718236760681178868` (single-cavity baseline) | `claim/EXT_hsp4_301_baseline.txt` (table ends at `N = 300: 0.187648382196`) | **`0.1875249820010892044888787`** | **`+0.0018885101774131363709919`** (`+1.888510e-03`) | `claim/EXT_hsp4_301.txt` | `29,220` | `88328e51d9077431491bacdc1be8b3db2b17753f3043c1709d071fb11ff224d8` |
| **Partial Win (`p3`, archive & contact audit)** | `hsp4` (`2..300`), `hsp5` (`2..300`), `hsp6` (`2..259`) | `856` listed rows across `hsp4`, `hsp5`, `hsp6` | Packomania coordinate tarballs | Uncovered 4D truncation bug in all `hsp5` (`299`) and `hsp6` (`249`) files + `9` missing `hsp6` files (`N=251..259`) | — | `claim/audit_report.txt` | `15,500` | `a25e4a219104a8176cc1cd64d1c05c51f090954262ef5cef7ab19bd9dda614aa` |

### Supporting Reference & Verification Artifacts in `claim/`
- `claim/CLAIM.md` (`6,338` bytes, SHA-256 `4b5c437d2e921565b773289d9d90e7ddb753894b1132f72f92ab3e35e997a2b2`)
- `claim/REPRODUCE.md` (`1,778` bytes, SHA-256 `3d6cb2f5d07861e2943dc57dcb319d45a8bc675b12e3a31b78ea3ccd6a830e12`)
- `claim/VERDICT.md` (`1,882` bytes, SHA-256 `4a6c4784c80b4009271af3cc36584a6391f9a6f0c8b2c3bffb6cfedbb70dee2e`)
- `claim/target.md` (`6,899` bytes, SHA-256 `cbde87d37030421382a9e4096275a0a7d778b46c20acdbb5004d7e86d22cd21b`)
- `claim/verify_hsp.py` (`14,942` bytes, SHA-256 `e05ada887bca7e11fe28e741376bc88c3f623dbb0f598aef3ef84f73c2a1b187`)
- `claim/EXT_hsp4_301_baseline.txt` (`29,220` bytes, SHA-256 `9c282b8426635a31344c2ed3ebcda53307f851df9d203fb37e4c7e6c6938857d`)
- `claim/ref_hsp4_170.txt` (`12,425` bytes, SHA-256 `ee9afeb72586d7237e9abe52f458f3ef629ba93b7466f5fb18c598560d6062d8`)
- `claim/ref_hsp4_300.txt` (`21,915` bytes, SHA-256 `fab48cff815b62e28502345b55d92231682443ccedd1837b3d6951a9df805ea3`)
- `claim/refetch_hsp4_radius.txt` (`5,575` bytes, SHA-256 `f3ddaa944aac014718bc9f5438700698abedac0189266198df8bb60772ac569f`)
- `claim/refetch_hsp4.html` (`88,618` bytes, SHA-256 `1c3a30644ba8ff73955547ff94e769a1983c146f4d2b14989eab3e0060a3feb3`)
- `claim/refetch_pending.html` (`4,954` bytes, SHA-256 `0d6ebbbe8e95abe7e701e1c70fbc1c0ec5bb06d611822b0b135ce3b776972384`)

---

## 4. Literature, Trophy Case & Open Pull Request Audit

1. **2024-2026 Literature Audit**:
   - The `hsp4`, `hsp5`, and `hsp6` tables on Packomania were first introduced by Eckard Specht in July-August 2025 (`04-Jul-2025` / `06-Jul-2025` for `hsp4`), combining classical small-$N$ constructions (Mackay 1980; Sloane, Hardin, and Smith spherical codes) with Specht's billiard/lubachevsky-stillinger optimization for $N \le 300$.
   - Web and literature searches for 2024-2026 publications on 4D equal hypersphere packings in a unit 4-ball at $N = 170$ or $N = 301$ confirm that no published paper or preprint improves upon Specht's `0.215589695168` bound at $N = 170$ or reports $N = 301$.
2. **`repo/TROPHY_CASE.md`**: Inspected in full (`12` entries total). None of the prior entries involve `packomania-hyperspheres-hsp4-hsp6` or 4D hypersphere packings in a container ball.
3. **Open Pull Requests (`elder-plinius/V3R1T4S`)**: Inspected all `100` open PRs returned by the GitHub API (`2026-10-14T12:00:19Z`). Zero open PRs target `packomania-hyperspheres-hsp4-hsp6`.

---

## 5. Summary Conclusion

The claimed 4D hypersphere packing at `d = 4, N = 170` (`claim/WIN_hsp4_170_polished.txt`, `r* = 0.2156450594683900081281903`) strictly beats the live Packomania record (`0.215589695168`) by `+5.536430e-05` (**553,643x** above the `1e-10` threshold), is provably non-isometric to the posted packing, and complies with the pending-queue rule (with the `26-Sep-2026 Moki & Julio *many* 4666 candidates` caveat explicitly noted). Both Partial Wins `p2` (`claim/EXT_hsp4_301.txt`) and `p3` (`claim/audit_report.txt`) are likewise verified as genuinely novel.

pass: true
