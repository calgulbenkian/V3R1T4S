# `2026-10-14-anonymous-c6d1e0ab-88328e51` — `packomania-hyperspheres-hsp4-hsp6` (`d = 4, N = 301`)

## What
Verified in 65-digit decimal arithmetic that object/EXT_hsp4_301.txt (29,220 bytes, SHA-256 88328e51d9077431491bacdc1be8b3db2b17753f3043c1709d071fb11ff224d8) defines a valid extension row packing of N = 301 equal 4D hyperspheres inside the unit 4D hypersphere with exact radius r* = 0.1875249820010892044888787, strictly exceeding the single-cavity insertion baseline 0.1856364718236760681178868 by +1.888510e-03 and sitting within 1.936e-05 of the N = 300 table value 0.187544340624 (Partial Win p2).

## Check It Yourself
```bash
bash verify-it-yourself/run_checks.sh
```

## Compared To
- **Primary Scoreboard (`https://packomania.com/hsp4/txt/radius.txt`, fetched `2026-10-14T11:09:08Z`, SHA-256 `f3ddaa944aac014718bc9f5438700698abedac0189266198df8bb60772ac569f`)**:
  - Standing bound: `0.1856364718236760681178868 (single-cavity insertion baseline; N=300 is 0.187544340624)`
  - Our certificate (`object/EXT_hsp4_301.txt`): `r* = 0.1875249820010892044888787` (`+0.0018885101774131363709919 (+1.888510e-03 over baseline, partial win p2)`)

## Not Claimed
- Does not claim optimality proof for `d = 4, N = 301`; provides an explicit 65-digit verified coordinate configuration. Note that `https://packomania.com/pending-requests.html` has `0` entries naming `hsp4`, `hsp5`, or `hsp6`, though it contains an uncategorized `*many*` batch entry (`26-Sep-2026 Moki & Julio *many* 4666 candidates`).

## Credits
- Reference tables and coordinate archives by Eckard Specht (`packomania.com`), N. J. A. Sloane, R. H. Hardin, W. D. Smith, and A. L. Mackay.
