# `2026-10-14-anonymous-c6d1e0ab-3536e50d` — `packomania-hyperspheres-hsp4-hsp6` (`d = 4, N = 170`)

## What
Verified in 65-digit decimal arithmetic that object/WIN_hsp4_170_polished.txt (16,513 bytes, SHA-256 3536e50dd047d04f09605dabb6bf33b5c17a9bfaf502147c2cc43c9da215bb65) defines a valid non-isometric packing of N = 170 equal 4D hyperspheres inside the unit 4D hypersphere with exact radius r* = 0.2156450594683900081281903, strictly exceeding the live Packomania hsp4 record 0.215589695168 (Eckard Specht) by +5.536430e-05 (553,643x the 1e-10 threshold).

## Check It Yourself
```bash
bash verify-it-yourself/run_checks.sh
```

## Compared To
- **Primary Scoreboard (`https://packomania.com/hsp4/txt/radius.txt`, fetched `2026-10-14T11:09:08Z`, SHA-256 `f3ddaa944aac014718bc9f5438700698abedac0189266198df8bb60772ac569f`)**:
  - Standing bound: `0.215589695168`
  - Our certificate (`object/WIN_hsp4_170_polished.txt`): `r* = 0.2156450594683900081281903` (`+0.0000553643003900081281903 (+5.536430e-05, 553,643x threshold)`)

## Not Claimed
- Does not claim optimality proof for `d = 4, N = 170`; provides an explicit 65-digit verified coordinate configuration. Note that `https://packomania.com/pending-requests.html` has `0` entries naming `hsp4`, `hsp5`, or `hsp6`, though it contains an uncategorized `*many*` batch entry (`26-Sep-2026 Moki & Julio *many* 4666 candidates`).

## Credits
- Reference tables and coordinate archives by Eckard Specht (`packomania.com`), N. J. A. Sloane, R. H. Hardin, W. D. Smith, and A. L. Mackay.
