# Connective constant of the 4.8^2 lattice: an exact-rational upper bound 18108999119/9912056861 = 1.826966832 (partial win p1, loop length 32)

## What

p1 only: a certified exact-rational upper bound mu(4.8^2) <= 18108999119/9912056861 = 1.826966831703 (loop length 32, 8,135,148 states, certificate = integer test vector with the automaton regenerated from AUTOMATON.md), below Jensen 2004 Table 3's 1.82926 (Alm's 1.829254) by about 2.29e-3, with a dated search of the indexed literature finding no later bound; it supersedes the author's k = 30 bound; subject to reproduce confirming the exact ratio from the vector.

(The last clause is the gate's own wording. The reproduce skeptic then confirmed the exact ratio from the vector; see panel/reproduce.md.)

The object is the positive integer test vector of a finite-memory loop-avoiding-walk automaton on the square-octagon (4.8^2) lattice. The states are not shipped: the checker regenerates the 8,135,148 states and rebuilds all 13,072,399 transitions from the definition in object/AUTOMATON.md, verifies the subset-inclusion condition of object/THEOREM.md on every one, and computes max (Px)_i / x_i exactly as a fraction.

## Check it yourself

From this package folder, run:

```sh
sh verify-it-yourself/run_checks.sh
```

- Requirements: python3 3.8 or later, standard library only; about 1.6 GB of memory and about 28 MB of temporary disk.
- Time: about 21 minutes on an idle Apple-silicon Mac (1,206 s for the whole script; the full check alone 1,193 s), longer on a slower or busy machine. A driver that enforces a timeout needs at least 3000 s (5400 s is safer on slow machines).
- Expected last line: ALL CHECKS PASS (the line before it is PASS, and above that: exact max (P x)_i / x_i = 18108999119 / 9912056861 = 18108999119/9912056861 = 1.826966831703).

The object is kept as 31 binary parts (27,851,812 bytes in all, each part at most 900,000 bytes) listed with their sha256 in object/SHA256_PARTS.txt. The script first checks every object file against SHA256SUMS, then reassembles the parts and checks the sha256 of the whole (90ff73f1cfa9702a47f15e59a2fcdbd02c28185f75c1bd309a4e44790c93390b) and of every part, runs a small known-answer test (loop length 22) and a negative control, and then runs the full check.

The submission id (2026-10-19-calgulbenkian-90ff73f1) takes its last eight hex digits from the sha256 of the main object, the reassembled whole vector file (the concatenation of object/vector_part_00.bin to vector_part_30.bin), which is 90ff73f1cfa9702a47f15e59a2fcdbd02c28185f75c1bd309a4e44790c93390b. The first eight hex digits of that hash are 90ff73f1.

## Compared to

The bar is Alm's published 1.829254. Jensen's Table 3 prints the same figure rounded as 1.82926.

| Source | Cell | Value | URL | UTC fetch time |
|---|---|---|---|---|
| S. E. Alm, J. Phys. A 38 (2005) 2055-2080, section 5.1.3 and summary table (manuscript copy read from the Internet Archive) | 4.8^2 rigorous upper bound | 1.829254 (the bar used here) | https://web.archive.org/web/2010id_/http://www2.math.uu.se/research/pub/Alm3.pdf | 2026-10-19T06:32:57Z |
| I. Jensen, J. Phys. A 37 (2004) 11521, Table 3 (arXiv cond-mat/0409381) | 4.8^2 upper bound | 1.82926 (Alm's figure, rounded; credited there to Alm via a private communication from Parviainen) | https://arxiv.org/pdf/cond-mat/0409381 | 2026-10-19T05:38:12Z |
| R. Parviainen, Uppsala Dissertations in Mathematics 34 (2004), thesis summary (Internet Archive copy) | no other 4.8^2 upper bound in the summary | none | https://web.archive.org/web/2020id_/http://uu.diva-portal.org/smash/get/diva2:164546/FULLTEXT01.pdf | 2026-10-19T06:37:18Z |
| arXiv API queries on connective constants of Archimedean lattices and Alm-type bounds, repeated by the novelty skeptic for this claim | no later 4.8^2 bound | none found | https://export.arxiv.org/api/query | 2026-10-19T14:34:34Z to 14:34:44Z |
| OpenAlex cited-by list for Alm 2005 | no later 4.8^2 bound among the 12 citing works | none found | https://api.openalex.org/works?filter=cites:W2040632682 | 2026-10-19T14:35:30Z |

This claim: 18108999119/9912056861 = 1.826966831703. Below Alm's 1.829254 by 2.287e-3 (below the rounded 1.82926 by 2.293e-3). The bank's required margin is 1e-6. Metadata for every fetch (HTTP status, sha256) and the full literature search are in the-record-we-beat/ and panel/novelty.md. The panel's criterion report is panel/criterion.md.

## Not claimed

- Only the 4.8^2 lattice and only loop length 32. No claim for the square lattice (the main criterion of the target), the triangular or kagome lattices, or any other loop length. The same team also reported a pocket-pruned loop length 34 bound (1.825523, option use_bridges = 2); no object is shipped for it, it is not covered by the theorem as stated, and it is not claimed.
- This is the partial win p1 only, not the target's main criterion.
- The bound rests only on the subset-inclusion condition (SI) proved in object/THEOREM.md, for locally finite vertex-transitive graphs. No claim that every loop up to length 32 is excluded by the automaton.
- The search for a later, better bound covered the indexed record only (Crossref, OpenAlex cited-by lists, arXiv queries, and the full texts of Jensen 2004, the weighted-SAW paper arXiv 2508.01993, Alm 2005 and a thesis summary). Google Scholar, MathSciNet, zbMATH, Scopus and Web of Science were not searched; Semantic Scholar returned HTTP 429 and was not retried. Absence of a better bound in unindexed or paywalled sources cannot be excluded. The dedicated search record was made for the k = 30 claim and was not repeated in full for k = 32: it is justified because any later bound beating 1.826967 would also have beaten the k = 30 bound, and the novelty and criterion skeptics re-ran fresh arXiv queries for this claim and found nothing new. Alm 2005 is read only as a manuscript copy from the Internet Archive, not the typeset journal page; Parviainen's thesis only as an 11-page summary from an archive copy; the novelty skeptic for k = 32 did not re-read either.
- The certificate (1.48 GB text file) was regenerated by the orchestrator from the author's generator (how-we-built-it/saw_bounds_2d.c, command saw_bounds_2d 482 32 cert_482_k32.txt 1, generator sha256 e49aab1197d5f061dbfff1c190b0b2a4bf1733f240c74c548627c8dc67cbf7fd) and is byte-identical (sha256 e6a346bd0a25d7ce1fb2e65df43854a7a07fa3499ce2fe47684d91e231e291ed) to the file on the author's laptop. Only its integer vector is shipped. The checker does not trust the generator: it regenerates the states and rebuilds the transitions from the definition, and the reproduce skeptic did the same with its own program (same states, same transitions, same exact ratio).
- The certificate is the vector alone; the states and transitions come from the written definition. This is a weaker form of certificate than a shipped transition list, and a reader whose regeneration differs on a tie-break would see the check fail rather than pass wrongly. Checking takes about 21 minutes and 1.6 GB.
- The definition had two ambiguous sentences found by the reproduce skeptic (rule 2 acts on the extended walk whose last vertex is the new neighbour; the offset of rule 3's suffix). They affect only which bound results, not its validity. object/AUTOMATON.md in this package carries a section "Clarifications added after the panel" stating both explicitly. The object and the checker are unchanged by it; the panel reviewed the object and checker before this text was added.
- Review of the theorem: at k = 30 a model of a different family (OpenAI gpt-6.1-sol) reviewed it read-only (clean with fixes, fixes applied); the theorem and rules are unchanged at k = 32, and the reproduce and criterion skeptics re-derived the proof at k = 32. This k = 32 package had no separate cross-family review.
- The three panel skeptics are Claude Code subagents; the object's builder (Gemini, Argon) is a different family from every skeptic. Not peer reviewed. The checker's lattice and symmetry checks run on a finite window and rely on period 3 of the lattice. The candidate-list caps (64, 32) and chord depth cap (3) are part of the definition: they decide which bound results, not its validity.
- The choice of loop length 32 is post hoc (the operator chose it to replace k = 30; k = 28 and 29 miss the target, k = 30 passes). The claim is one exact certified number.

## Filing history

This package replaces the loop length 30 package inside open pull request #534, on the operator's in-session instruction to update #534 in place. That earlier package claimed the k = 30 bound 849051343/464433440 = 1.8281442934 and was first filed in #534 on 2026-10-19 with the package 2026-10-19-calgulbenkian-5b68e2eb. The k = 32 bound is strictly stronger than the k = 30 bound (1.826966831703 < 1.828144293400), with the same theorem and the same rules; only the loop length differs, and the object is stored as the test vector alone instead of the state list. #534 is not a refile of a closed pull request. Nothing has been pushed or posted from this folder.

## Credits

- **Sven Erick Alm**, "Upper and lower bounds for the connective constants of self-avoiding walks on the Archimedean and Laves lattices", J. Phys. A 38 (2005) 2055-2080 (section 5.1.3: mu < 1.829254 for the 4.8^2 lattice; the transfer-matrix upper-bound method), read from https://web.archive.org/web/2010id_/http://www2.math.uu.se/research/pub/Alm3.pdf and his page https://www2.math.uu.se/~sveralm/boundsabstr.html. This is the bar we compare against.
- **Robert Parviainen**, thesis "Connectivity Properties of Archimedean and Laves Lattices", Uppsala Dissertations in Mathematics 34 (2004), which contains the joint paper with Alm (listed in its summary as "Sven Erick Alm and Robert Parviainen"); the figure 1.82926 in Jensen's table is credited to Alm via Parviainen's private communication. https://uu.diva-portal.org/smash/get/diva2:164546/FULLTEXT01.pdf (read from an Internet Archive copy).
- **Iwan Jensen**, "Improved lower bounds on the connective constants for two-dimensional self-avoiding walks", J. Phys. A 37 (2004) 11521, https://arxiv.org/abs/cond-mat/0409381: Table 3, where the 4.8^2 upper bound 1.82926 is listed.
- **Andre Ponitz and Peter Tittmann** (2000): the finite-memory automaton for square-lattice self-avoiding walks that the bank statement names; the automaton used here is a finite-memory loop-avoiding-walk automaton of that kind, and we have not read their paper.
- **Olivier Couronne**, arXiv 2211.16146 (2022), a modified finite-memory automaton for the square lattice, and the open weighted_connective_constant software with its paper arXiv 2508.01993 (Qidong He, J. Phys. A 58 (2025) 505003, as the bank statement gives it) were read and searched as the claim's sources; neither contains a 4.8^2 bound and neither's code was used.
- Contributor credit: calgulbenkian. The search code is by the contributor's AI search agent (Gemini, called Argon); see how-we-built-it/.
