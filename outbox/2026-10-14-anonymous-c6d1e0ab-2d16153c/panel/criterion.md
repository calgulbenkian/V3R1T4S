# CRITERION Skeptic Report: `snake-coil-in-the-box` (`PARTIAL_PROGRESS` on `p1`, `p2`, and `p3`)

context: subagent
confirmed_scope: Verified 11 explicit hypercube induced-path and induced-cycle certificates in claim/ achieving Partial Wins p1 (symmetric coils in Q_12 of length 1,450 beating live minortriad 1,434 by +16 edges and in Q_13 of length 2,870 beating live minortriad 2,830 by +40 edges), p2 (Q_14 coil of length 5,854 beating published 5,750 by +104 edges and Q_14 snake of length 5,854 beating published 5,850 by +4 edges), and p3 (7 equal-record snakes and coils in Q_10 through Q_13 strictly inequivalent under hypercube automorphisms, reversal, and cyclic rotation to all published reference records), with length-convention calibration verified across all 37 minortriad and published reference records.

## 1. Clause-by-Clause Verification Against `claim/target.md`

### 1.1 Length-Convention Calibration (`claim/verify_snake.py --calibrate`)
- Executed `python3 claim/verify_snake.py --calibrate --seeds-dir data/seeds`.
- Confirmed exact reproduction of the edge length, snake/coil type, and symmetric-coil half-period invariance (`steps[:L//2] == steps[L//2:]`) across all 37 `minortriad.com` reference records (`sn1`..`sn13`, `co2`..`co13`, `sc2`..`sc13`) as well as `toner_q13_2946.txt` (`n=13`, snake, `L=2946`), `toner_q14_5850.txt` (`n=14`, snake, `L=5850`), and `taylor_coil_Q14.json` (`n=14`, coil, `L=5750`).

### 1.2 Partial Win `p1`: Symmetric-Coil World Records in $Q_{12}$ and $Q_{13}$
- **Criterion (`p1`)**: A coil in $Q_n$ ($9 \le n \le 13$) that is invariant under the symmetry required by the `minortriad` symmetric-coil table (`steps[:L//2] == steps[L//2:]`), verified exhaustively, whose length strictly exceeds the live `minortriad` symmetric-coil value for that $n$ ($Q_{12}: 1,434$; $Q_{13}: 2,830$, re-fetched `2026-10-14T10:14:48Z`, SHA-256 `af45d6499dcae6cb6d3e1942c5ccd0ab8159c7755dec1667e097a1859dfcebb2`).
- **Verified artifacts**:
  1. `claim/sym_coil_Q12_1450.txt` (`1,451` bytes, SHA-256 `99b1ed6796d7742edbc672164214e4bc6b3a9e0ccd7b4d62a9159936d9339606`): Exhaustively verified induced cycle in $Q_{12}$ (`used_dims=12`, `symmetric=True`) of length **`L = 1,450`**, strictly beating `1,434` by **`+16` edges**.
  2. `claim/sym_coil_Q13_2870.txt` (`2,871` bytes, SHA-256 `916098a5643395c31ff6ee83b41ba473c9c177fda1b1a6e52689f9ce1ce66eea`): Exhaustively verified induced cycle in $Q_{13}$ (`used_dims=13`, `symmetric=True`) of length **`L = 2,870`**, strictly beating `2,830` by **`+40` edges** (alongside secondary symmetric coil `claim/sym_coil_Q13_2846.txt`, SHA-256 `c625b96ed05fc23149baddf52a8584742235c47c5d75010cffb3054f9a094853`, `L = 2,846`, `+16` edges).

### 1.3 Partial Win `p2`: $Q_{14}$ Coil and Snake World Records
- **Criterion (`p2`)**: A snake or coil in $Q_{14}$, verified exhaustively, strictly longer than every $Q_{14}$ value published at verification time (`arXiv:2609.27483`, `tommyet/snakes`, `williamtoner/SnakeBox`, where published records are $5,750$ for $Q_{14}$ coil and $5,850$ for $Q_{14}$ snake).
- **Verified artifacts**:
  3. `claim/coil_Q14_5854.txt` (`5,855` bytes, SHA-256 `508e47a18fd5083e40dd391b22f8df564f02cc9295af99977ac17e371e26b3c7`): Exhaustively verified induced cycle in $Q_{14}$ (`used_dims=14`) of length **`L = 5,854`**, strictly beating the published $Q_{14}$ coil record `5,750` by **`+104` edges**.
  4. `claim/snake_Q14_5854.txt` (`5,855` bytes, SHA-256 `47e5e3f6ef0d9d68065090f8749a15281151755cf453495da3669b4336b61935`): Exhaustively verified induced path in $Q_{14}$ (`used_dims=14`) of length **`L = 5,854`**, strictly beating William Toner's Oct 12, 2026 $Q_{14}$ snake record `5,850` by **`+4` edges**.

### 1.4 Partial Win `p3`: 7 Equal-Record Strictly Inequivalent Snakes and Coils in $Q_{10}..Q_{13}$
- **Criterion (`p3`)**: Length equal to the live record for that $n$ and type ($9 \le n \le 13$), verified exhaustively, and inequivalent under hypercube automorphisms (coordinate permutations and translations) and reversal (plus cyclic rotation for coils) to every record file published in `minortriad.com`, `Math-AI-Caltech/Snake-in-the-Box`, `williamtoner/SnakeBox`, and `tommyet/snakes`, checked by comparing canonical relabelled transition sequences (`claim/verify_snake.py --check-inequiv`).
- **Verified artifacts**:
  5. `claim/inequiv_co10_374.txt` (`375` bytes, SHA-256 `f1a736ab0fcc62757d46850b884bcd6c80460bebced6d2f25c6eaef1d5380755`): $Q_{10}$ coil, `L = 374`, `STRICTLY INEQUIVALENT` to all 13 reference entries (12 canonical classes).
  6. `claim/inequiv_co11_740.txt` (`741` bytes, SHA-256 `3f22401b0f8250eccca65436ed4564f858bbb58e76e16da4dee6a77e5600b42d`): $Q_{11}$ coil, `L = 740`, `STRICTLY INEQUIVALENT` to reference bank.
  7. `claim/inequiv_co12_1468.txt` (`1,469` bytes, SHA-256 `a4b75c268608c66ec436a4b9735ac85d009462ea2e2d6e52f8d7398dd69bb198`): $Q_{12}$ coil, `L = 1,468`, `STRICTLY INEQUIVALENT` to reference bank.
  8. `claim/inequiv_co13_2930.txt` (`2,931` bytes, SHA-256 `342cc9c7a9f90b1d336f88ab2a49428d58d676f7b779d59723cdfdcc1d9498db`): $Q_{13}$ coil, `L = 2,930`, `STRICTLY INEQUIVALENT` to reference bank.
  9. `claim/inequiv_sn11_750.txt` (`751` bytes, SHA-256 `78c2a47f837e8e4bcea2a5a69782233ee968e71cb5c7660a0e44f2d2f660b695`): $Q_{11}$ snake, `L = 750`, `STRICTLY INEQUIVALENT` to reference bank.
  10. `claim/inequiv_sn12_1480.txt` (`1,481` bytes, SHA-256 `2d16153c21433d994b8d787fdd360e877fd3737f96e70a4feded6975bacdaa03`): $Q_{12}$ snake, `L = 1,480`, `STRICTLY INEQUIVALENT` to reference bank.
  11. `claim/inequiv_sn13_2946.txt` (`2,947` bytes, SHA-256 `1708be3f455e2bbb75681d98e33aab6b3c533632085db9926974037eb6c41d1d`): $Q_{13}$ snake, `L = 2,946`, `STRICTLY INEQUIVALENT` to all 2 reference entries.

## 2. Verdict
All literal clauses of Partial Wins `p1`, `p2`, and `p3` in `claim/target.md` are satisfied.

pass: true
