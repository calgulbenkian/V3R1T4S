# How We Found It (`degree-diameter-table`: `(14, 3)` at `N = 1,117`)

*(contributor text, unverified)*

1. **Unused Degree-Slack Audit (`Lens 1: symmetry-orbit-join`)**:
   Inspecting the live `D = 3` adjacency lists on the Comellas degree-diameter server revealed that the standing `(14, 3)` record graph (`deg14_diam3_n1116_adjlist.txt`, `N_0 = 1,116`) is not 14-regular: it has `998` vertices of degree `14` and `118` vertices of degree `13` (`118` unused degree-14 edge slots), whose 2-balls cover every vertex of `G_0` with multiplicity at least `4`.
2. **Slack-Preserving 2-Ball Warm Start + Native C Simulated Annealing (`how-we-built-it/sa2_opt.c`)**:
   We inserted vertex `1116` (`N = 1,117`) and greedily connected it to `14` degree-13 vertices maximizing 2-ball coverage in `G_0` while leaving the remaining `104` free degree-14 slots on `0..1115` open. This warm start produced an initial `1,117`-vertex graph with only `29` unordered vertex pairs at distance `> 3` out of `623,286` pairs. Our native C bit-parallel BFS + simulated annealing optimizer (`how-we-built-it/sa2_opt.c`) then applied pure edge additions between degree-13 vertices and targeted 2-switches across distance layers `i + j = 2`, reducing the `29` bad pairs to `0` in `11.53` seconds (`48` accepted moves).
