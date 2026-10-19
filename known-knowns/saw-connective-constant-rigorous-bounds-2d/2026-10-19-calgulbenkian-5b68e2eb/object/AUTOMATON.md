# Definition of the automaton and of the state file

All of this is also implemented, from this text alone, in verify-it-yourself/check_saw482.py.

## Lattice
Vertices: integer points (x, y) with (x mod 3, y mod 3) one of (1,0) type E, (2,0) type W, (0,1) type N, (0,2) type S. Neighbours (offsets), in this fixed order:
- E: (-1,+1), (-1,-1), (+1,0)
- N: (+1,-1), (-1,-1), (0,+1)
- W: (+1,+1), (+1,-1), (-1,0)
- S: (+1,+1), (-1,+1), (0,-1)
This is the 4.8^2 lattice (every vertex has degree 3). dist is graph distance.

## Automorphisms used
sigma = translation by (3a, 3b) composed with one of 8 symmetries g_s about the origin: for s = 0..7, first sx = -x if bit 0 of s else x; sy = -y if bit 1 of s else y; then (sy, sx) if bit 2 else (sx, sy).

## Walks and states
A walk is a list of distinct vertices, consecutive ones adjacent, oldest first, head last. Its canonical key: let (ax, ay) be the head, rx = ax mod 3, ry = ay mod 3, tx = ax - (-1 if rx == 2 else rx), ty = likewise. Translate all points by (-tx, -ty), apply each of the 8 symmetries, and keep the symmetry whose coordinate sequence (x, then y, of the head, then of the previous point, and so on back to the oldest) is lexicographically smallest. The head of a canonical walk is therefore always (-1, 0). A state is a canonical walk.

Loop length k = 30 (K in the checker). prune(walk): drop oldest vertices one at a time (start = 0, 1, ...) while start < len - 2 and (len - 1 - start) + dist(walk[start], head) > k; the result walk[start:] is canonicalised.

## Seeds
The canonical forms of the walks [(1,0),(0,1)] (square edge) and [(1,0),(2,0)] (octagon edge).

## Transitions (rebuilt by the checker)
For a state with vertex set V and head h, and each neighbour A of h with A not in V, let ext = walk + [A]. Candidate targets:
1. c0 = prune(ext).
2. If (len(ext) - 1) + dist(ext[0], A) > k: chord shortcuts. For a from min_a (initially 0) up to len(walk) - 4 and, for each b with a + 2 <= b <= len(walk) - 2 in increasing order, such that walk[a] and walk[b] are adjacent: the shortcut sx = walk[0..a] + walk[b..end] gives candidate prune(sx) (added if not already a candidate and fewer than 64 candidates); and if the recursion depth is below 3 and (len(sx) - 1) + dist(sx[0], head) > k, recurse on sx with depth + 1 and min_a = a. (Here walk means the walk being examined at that level, and its last vertex is the new head.)
3. Also, if (len(ext) - 1) + dist(ext[0], A) > k: for start = 0, 1, ... while start < len(ext) - 2 and (len(ext) - 1 - start) + dist(ext[start], A) > k, the canonical form of ext[start:] is a further candidate if it is in the state list (and fewer than 32 candidates so far).
The target is the candidate with the smallest test-vector entry. Candidates that are not in the state list are an error for 1 and 2 (the list must be closed under them).
Each chosen target is verified to satisfy the subset-inclusion invariant (THEOREM.md) against the state decoded from the file.

## State file (object/states_part_NN.bin concatenated, in this order)
A sequence of records, one per state, no header and no separator:
- 1 byte: L, the number of vertices of the state (1 to 63).
- 6 bytes, big-endian: the test-vector entry V (a positive integer below 2^48).
- ceil(2(L-1)/8) bytes, big-endian integer "bits": for i = 0 .. L-2, the 2-bit field (bits >> 2i) & 3 is the index (0, 1 or 2, in the neighbour order above) of the next vertex backwards from the current one, starting at the head (-1, 0). So vertex i steps back along neighbour number d_i.
The number of records is 2,750,336 for k = 30. Decoding gives the walk oldest first.
