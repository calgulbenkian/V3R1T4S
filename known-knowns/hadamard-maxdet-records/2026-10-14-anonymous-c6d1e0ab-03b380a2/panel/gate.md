# Verification Gate Verdict: Hadamard MaxDet Order `n = 81` (`p2_81`)

- `reproduce.md`: `pass: true` (`context: subagent`)
- `novelty.md`: `pass: true` (`context: subagent`)
- `criterion.md`: `pass: true` (`context: subagent`)

status: CONFIRMED_PARTIAL
confirmed_scope: Verified that claim/G81_p2.json (192,478 bytes, SHA-256 03b380a2074785deac39cb19b68c0853cd52ea469f7b848600cc756df42c8992) defines a valid Partial Win p2 (Frozen Gram Target) at order n = 81 consisting of an 81x81 symmetric positive-definite integer Gram matrix G with diagonal 81, valid pairwise and triple mod-4 congruences, exact normalized root-determinant sqrt(det G) / 2^80 = 252 * 20^39 = 138538465099776000000000000000000000000000000000000000 strictly beating the live record 196 * 20^39 = 107752139522048000000000000000000000000000000000000000, constructive exact rational congruence P (81 I_81) P^T = G (and Q Q^T = G), and 80 realized {-1,+1} rows M0 matching the leading 80x80 principal block of G.
