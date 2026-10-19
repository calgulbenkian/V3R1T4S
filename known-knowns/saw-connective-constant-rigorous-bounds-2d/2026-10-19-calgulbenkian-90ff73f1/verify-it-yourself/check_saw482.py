"""Standard-library checker for the (4.8^2) lattice self-avoiding-walk upper bound certificate, loop length K = 32.

Usage: python3 -I check_saw482.py VECTOR_BIN K [--limit N] [--dump FILE]

VECTOR_BIN is the reassembled object/vector_part_*.bin (format: object/AUTOMATON.md).  The object holds ONLY the
positive integer test vector.  This program
  1. regenerates the state set itself, breadth-first from the two seed states, in the canonical order of
     object/AUTOMATON.md (the order of the vector's entries);
  2. rebuilds, for every state and every free neighbour of its head, the candidate target states from the
     definition in AUTOMATON.md (suffix pruning with exact graph distance, chord shortcuts, intermediate suffixes);
  3. takes the candidate with the smallest vector entry and verifies for EVERY transition that the
     subset-inclusion invariant (object/THEOREM.md) holds against the target state;
  4. computes the exact maximum of (P x)_i / x_i over EVERY state by integer cross-multiplication.
Last line: PASS or FAIL.  --limit N processes only the first N states in step 2-4 (smoke test; never prints PASS).
"""
import sys, time, lzma
from array import array
from fractions import Fraction

K = int(sys.argv[2])
LIMIT = None
if '--limit' in sys.argv: LIMIT = int(sys.argv[sys.argv.index('--limit') + 1])
BOUND_TO_BEAT = Fraction(182926, 100000) - Fraction(2, 1000000)   # 1.82926 - 2e-6
K30_BOUND = Fraction(849051343, 464433440)                        # the previously claimed loop-length-30 bound
# Claims by loop length K: (number of states, exact bound).  K = 32 is the claim; K = 22 is a small known-answer
# test of the same code (the exact bound of the author's generator at k = 22, which is also computed by this file).
CLAIMS = {32: (8135148, Fraction(18108999119, 9912056861)),
          22: (39367, Fraction(693444578290, 377832855505))}

# ---------------------------------------------------------------- lattice
OFF = {  # neighbour offsets by vertex type, in the order used throughout
    'E': ((-1, 1), (-1, -1), (1, 0)), 'N': ((1, -1), (-1, -1), (0, 1)),
    'W': ((1, 1), (1, -1), (-1, 0)), 'S': ((1, 1), (-1, 1), (0, -1))}
TYPE = {(1, 0): 'E', (2, 0): 'W', (0, 1): 'N', (0, 2): 'S'}
NBR_CACHE = {}
def nbrs(p):
    r = NBR_CACHE.get(p)
    if r is None:
        t = TYPE[(p[0] % 3, p[1] % 3)]
        r = tuple((p[0] + a, p[1] + b) for a, b in OFF[t])
        if len(NBR_CACHE) < 3000000: NBR_CACHE[p] = r
    return r
def is_vertex(p): return (p[0] % 3, p[1] % 3) in TYPE

def g(s, x, y):  # the 8 symmetries about the origin
    sx = -x if s & 1 else x
    sy = -y if s & 2 else y
    return (sy, sx) if s & 4 else (sx, sy)

# graph distance by breadth-first search from the four vertex types of the cell at the origin
DT = {}
for rep in TYPE:
    d = {rep: 0}; frontier = [rep]
    for depth in range(1, K + 6):
        nxt = []
        for p in frontier:
            for q in nbrs(p):
                if q not in d: d[q] = depth; nxt.append(q)
        frontier = nxt
    DT[rep] = d
def dist(p, q):
    bx = p[0] - p[0] % 3; by = p[1] - p[1] % 3
    return DT[(p[0] % 3, p[1] % 3)].get((q[0] - bx, q[1] - by), 9999)

fails = []
def check(ok, msg):
    print(('ok   ' if ok else 'FAIL ') + msg, flush=True)
    if not ok: fails.append(msg)

def lattice_checks():
    ok = True
    for x in range(-9, 10):
        for y in range(-9, 10):
            if not is_vertex((x, y)): continue
            for q in nbrs((x, y)):
                ok &= is_vertex(q) and (x, y) in nbrs(q)
            for s in range(8):  # symmetries and translations by 3Z^2 are automorphisms
                gp = g(s, x, y)
                ok &= is_vertex(gp) and sorted(g(s, *q) for q in nbrs((x, y))) == sorted(nbrs(gp))
            ok &= sorted((a + 3, b - 6) for a, b in nbrs((x, y))) == sorted(nbrs((x + 3, y - 6)))
    check(ok, 'lattice: adjacency symmetric and 3-regular; the 8 symmetries about the origin and translations by 3Z^2 are automorphisms (window +-9)')

def canon_key(walk):
    """Canonical key of a walk (list of points, oldest first, head last): bytes of the coordinates from head backwards."""
    L = len(walk); ax, ay = walk[-1]
    rx = ax % 3; ry = ay % 3
    tx = ax - (-1 if rx == 2 else rx); ty = ay - (-1 if ry == 2 else ry)
    cands = list(range(8))
    for i in range(L - 1, -1, -1):
        x = walk[i][0] - tx; y = walk[i][1] - ty
        vals = [(g(s, x, y), s) for s in cands]
        m = min(v for v, _ in vals)
        cands = [s for v, s in vals if v == m]
        if len(cands) == 1: break
    s = cands[0]
    out = bytearray()
    for i in range(L - 1, -1, -1):
        x, y = g(s, walk[i][0] - tx, walk[i][1] - ty)
        out.append(x + 64); out.append(y + 64)
    return bytes(out)

def key_points(key):
    """Canonical key -> points, oldest first."""
    return [(key[i] - 64, key[i + 1] - 64) for i in range(len(key) - 2, -2, -2)]

def prune_key(walk):
    wL = len(walk); head = walk[-1]; start = 0
    while start < wL - 2:
        if (wL - 1 - start) + dist(walk[start], head) <= K: break
        start += 1
    return canon_key(walk[start:])

INDEX = {}; KEYS = []
def register(key):
    j = INDEX.get(key)
    if j is None:
        j = len(KEYS); INDEX[key] = j; KEYS.append(key)
    return j

def chords(walk, depth, min_a, cands, maxc=64):
    """Chord shortcuts, in the order of AUTOMATON.md.  Every shortcut's pruned state is registered (it is a state of
    the automaton); it becomes a candidate if not yet one and fewer than maxc candidates exist."""
    wL = len(walk)
    idx = {p: i for i, p in enumerate(walk)}
    for a in range(min_a, wL - 3):
        bs = sorted(b for b in (idx.get(q) for q in nbrs(walk[a])) if b is not None and a + 2 <= b <= wL - 2)
        for b in bs:
            sx = walk[:a + 1] + walk[b:]
            j = register(prune_key(sx))
            if j not in cands and len(cands) < maxc: cands.append(j)
            if depth < 3 and (len(sx) - 1) + dist(sx[0], sx[-1]) > K:
                chords(sx, depth + 1, a, cands, maxc)

def invariant(vset, A, target):
    """exists sigma = (symmetry, translation in 3Z^2) with sigma(A) = head(target) and V(target) within sigma(V + A)."""
    hj = target[-1]
    for s in range(8):
        ga = g(s, *A)
        tx = hj[0] - ga[0]; ty = hj[1] - ga[1]
        if tx % 3 or ty % 3: continue
        img = {(g(s, *q)[0] + tx, g(s, *q)[1] + ty) for q in vset}
        img.add(hj)
        if all(t in img for t in target): return True
    return False

def decode_vector(blob):
    """object format: the 8 bytes SAW482V2, then one lzma (xz) stream holding six planes of N bytes each; plane j
    holds byte j (most significant first) of the 48-bit big-endian integer x_i.  N = decompressed length / 6."""
    assert blob[:8] == b'SAW482V2'
    raw = lzma.decompress(blob[8:])
    N = len(raw) // 6
    assert 6 * N == len(raw)
    P = [raw[j * N:(j + 1) * N] for j in range(6)]
    return [(P[0][i] << 40) | (P[1][i] << 32) | (P[2][i] << 24) | (P[3][i] << 16) | (P[4][i] << 8) | P[5][i] for i in range(N)]

def pass1(t0):
    # pass 1: regenerate the state set breadth-first (square seed, then octagon seed), recording the
    #      candidates of rules 1 and 2 for every transition
    register(canon_key([(1, 0), (0, 1)])); register(canon_key([(1, 0), (2, 0)]))   # square seed, octagon seed
    CAND = array('i'); CNT = array('B')       # flat candidate indices, and the number of candidates of each transition
    i = 0
    while i < len(KEYS):
        pts = key_points(KEYS[i]); vset = set(pts); head = pts[-1]
        for A in nbrs(head):
            if A in vset: continue
            ex = pts + [A]
            c0 = register(prune_key(ex))
            cands = [c0]
            if (len(ex) - 1) + dist(ex[0], A) > K: chords(ex, 1, 0, cands)
            CNT.append(len(cands)); CAND.extend(cands);
        i += 1
        if i % 1000000 == 0: print('   pass 1: %d states done, %d known, %.0fs' % (i, len(KEYS), time.time() - t0), flush=True)
    return CAND, CNT

def main():
    t0 = time.time()
    blob = open(sys.argv[1], 'rb').read()
    lattice_checks()
    Vs = decode_vector(blob)
    N = len(Vs)
    print('vector entries read: %d, bytes %d, decode %.0fs' % (N, len(blob), time.time() - t0), flush=True)
    check(min(Vs) > 0, 'all test-vector entries are positive integers (min %d, max %d)' % (min(Vs), max(Vs)))
    # ---- seeds: every directed edge of the lattice is equivalent to one of two seed states
    seed_sq = canon_key([(1, 0), (0, 1)]); seed_oct = canon_key([(1, 0), (2, 0)])
    edge_keys = set()
    for x in range(-12, 13):
        for y in range(-12, 13):
            if is_vertex((x, y)):
                for q in nbrs((x, y)): edge_keys.add(canon_key([(x, y), q]))
    check(edge_keys == {seed_sq, seed_oct}, 'all directed edges in window +-12 reduce to the two seed states (%d classes)' % len(edge_keys))
    heads = set()
    for x in range(-12, 13):
        for y in range(-12, 13):
            if is_vertex((x, y)): heads.add(canon_key([(x, y)]))
    check(len(heads) == 1, 'all vertices in the window are equivalent under the symmetry group (vertex-transitive): %d class' % len(heads))
    CAND, CNT = pass1(t0)
    check(len(KEYS) == N, 'regenerated state count %d equals the vector length %d' % (len(KEYS), N))
    if len(KEYS) != N:
        print('FAIL (%d)' % len(fails)); return 1
    print('pass 1 done: %d states, %d transitions, %.0fs' % (N, len(CNT), time.time() - t0), flush=True)
    # ---- pass 2: add rule 3 candidates (intermediate suffixes already in the state list), choose the smallest
    #      vector entry, verify subset-inclusion on every chosen transition, exact ratio
    best_n, best_d, best_i = 0, 1, -1
    ntrans = 0; bad_inv = 0; multi = 0; nonc0 = 0; maxcand = 0
    ci = 0; ti = 0
    limit = N if LIMIT is None else min(N, LIMIT)
    dump = None
    for i in range(N):
        if i >= limit: break
        pts = key_points(KEYS[i]); vset = set(pts); head = pts[-1]
        V = Vs[i]; total = 0
        for A in nbrs(head):
            if A in vset: continue
            cnt = CNT[ti]; ti += 1
            cands = list(CAND[ci:ci + cnt]); ci += cnt
            ex = pts + [A]; ntrans += 1
            if (len(ex) - 1) + dist(ex[0], A) > K:
                newL = len(ex)
                for start in range(0, newL - 2):
                    if (newL - 1 - start) + dist(ex[start], A) <= K: break
                    j = INDEX.get(canon_key(ex[start:]))
                    if j is not None and j not in cands and len(cands) < 32: cands.append(j)
            maxcand = max(maxcand, len(cands))
            if len(cands) > 1: multi += 1
            jbest = min(cands, key=lambda j: Vs[j])
            if jbest != cands[0]: nonc0 += 1
            if not invariant(vset, A, key_points(KEYS[jbest])):
                bad_inv += 1
                if bad_inv < 4: print('   invariant FAILS at state', i)
            total += Vs[jbest]
        if total * best_d > best_n * V: best_n, best_d, best_i = total, V, i
        if i % 1000000 == 0 and i: print('   pass 2: %d states, %.0fs' % (i, time.time() - t0), flush=True)
    print('transitions rebuilt %d, with more than one candidate %d, using a candidate other than the plain suffix %d, max candidates %d' % (ntrans, multi, nonc0, maxcand))
    check(bad_inv == 0, 'subset-inclusion invariant holds on all %d chosen transitions (failures: %d)' % (ntrans, bad_inv))
    r = Fraction(best_n, best_d)
    print('exact max (P x)_i / x_i = %d / %d = %s = %.12f  (state index %d)' % (best_n, best_d, r, float(r), best_i))
    if LIMIT is not None:
        print('SMOKE TEST ONLY (--limit)'); return 2
    if K not in CLAIMS:
        print('no claim recorded for K = %d' % K); return 2
    nclaim, rclaim = CLAIMS[K]
    check(N == nclaim, 'state count %d equals the claimed %d' % (N, nclaim))
    check(r == rclaim, 'bound equals the claimed %s exactly (got %s)' % (rclaim, r))
    if K == 32:
        check(r < BOUND_TO_BEAT, 'bound %s < 1.82926 - 2e-6 (exact rational comparison)' % r)
        check(r < K30_BOUND, 'bound %s < the loop-length-30 bound 849051343/464433440 (exact rational comparison)' % r)
    else:
        print('known-answer test only (K = %d): not the claimed loop length' % K)
    print('elapsed %.0f s' % (time.time() - t0))
    print('PASS' if not fails else 'FAIL (%d)' % len(fails))
    return 0 if not fails else 1
if __name__ == '__main__':
    sys.exit(main())
