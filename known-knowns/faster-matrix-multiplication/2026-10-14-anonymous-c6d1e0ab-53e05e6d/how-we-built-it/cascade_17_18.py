#!/usr/bin/env python3
"""cascade_17_18.py -- Generalized rank-1 slice peeling + iterated Rado-Edmonds matroid
max-kill nullspace absorption cascade on LITA 17x17x17_r2723, 18x18x18_r3031, and 16x16x16_r2236.
"""
import ast, hashlib, json, os, struct, sys, time, zipfile
from collections import Counter
from fractions import Fraction

sys.path.insert(0, os.path.abspath("repo/known-knowns/faster-matrix-multiplication/how-we-built-it"))
sys.path.insert(0, os.path.abspath("runs/2026-10-14-0425"))
sys.path.insert(0, os.path.abspath("runs/2026-10-14-0425/attempts/representation-absorber/code"))

import peel as PEEL
import screen_all as SA
import verify_brent as VB


def load_lita_npz_stdlib(path):
    arrays = {}
    meta = None
    with zipfile.ZipFile(path, "r") as zf:
        for name in zf.namelist():
            if not name.endswith(".npy"):
                continue
            key = name[:-4]
            data = zf.read(name)
            major = data[6]
            if major == 1:
                hdr_len = struct.unpack("<H", data[8:10])[0]
                offset = 10 + hdr_len
                hdr_str = data[10:offset].decode("latin1").strip()
            else:
                hdr_len = struct.unpack("<I", data[8:12])[0]
                offset = 12 + hdr_len
                hdr_str = data[12:offset].decode("latin1").strip()
            hdr = ast.literal_eval(hdr_str)
            descr = hdr["descr"]
            body = data[offset:]
            if key == "metadata_json":
                meta = json.loads(body.decode("utf-32-le"))
                continue
            if "i8" in descr or "u8" in descr:
                fmt_ch, sz = ("q" if "i" in descr else "Q"), 8
            elif "i4" in descr or "u4" in descr:
                fmt_ch, sz = ("i" if "i" in descr else "I"), 4
            elif "i2" in descr or "u2" in descr:
                fmt_ch, sz = ("h" if "i" in descr else "H"), 2
            elif "i1" in descr or "u1" in descr or "b" in descr:
                fmt_ch, sz = "b", 1
            else:
                raise ValueError(f"Unsupported dtype {descr} for {key}")
            cnt = len(body) // sz
            arrays[key] = struct.unpack("<" + fmt_ch * cnt, body)
    n1, n2, n3 = [int(x) for x in meta["tensor"]]
    r = int(meta["rank"])

    def axis(name, cols):
        indptr = arrays[f"{name}_indptr"]
        idx = arrays[f"{name}_indices"]
        num = arrays[f"{name}_numerators"]
        den = arrays[f"{name}_denominators"]
        rows = []
        for q in range(len(indptr) - 1):
            row = [Fraction(0)] * cols
            for t in range(int(indptr[q]), int(indptr[q + 1])):
                row[int(idx[t])] += Fraction(int(num[t]), int(den[t]))
            rows.append(row)
        return rows

    u = axis("u", n1 * n2)
    v = axis("v", n2 * n3)
    w_c = axis("w", n1 * n3)
    w = []
    for row in w_c:
        wt = [Fraction(0)] * (n3 * n1)
        for i in range(n1):
            for l in range(n3):
                wt[l * n1 + i] = row[i * n3 + l]
        w.append(wt)
    return (n1, n2, n3), u, v, w, {"declared_rank": r, "z2": False, "lita_metadata": meta}


PEEL.load_lita_npz = load_lita_npz_stdlib

RES_DIR = "runs/2026-10-14-0425/attempts/representation-absorber/result"
os.makedirs(RES_DIR, exist_ok=True)

# Standing bars from fmm_sota.json and fmm.univ-lille.fr/<n>x<m>x<p>.html
SOTA_BARS = {
    (16, 17, 17): (2723, 2738),
    (16, 16, 17): (2492, 2560),
    (15, 17, 17): (2622, 2622),
    (15, 16, 17): (2448, 2448),
    (15, 15, 17): (2320, 2320),
    (14, 16, 17): (2306, 2306),
    (14, 17, 17): (2456, 2456),
    (17, 18, 18): (3031, 3175),
    (17, 17, 18): (3012, 3080),
    (16, 17, 18): (2884, 2884),
    (16, 18, 18): (2916, 2916),
    (15, 15, 16): (2132, 2132),
    (15, 16, 16): (2180, 2223),
    (16, 16, 16): (2236, 2236),
}


def canonicalize_dims(fmt, u, v, w):
    n1, n2, n3 = fmt
    r = len(u)
    U = [PEEL.mat_of(u[k], n1, n2) for k in range(r)]
    V = [PEEL.mat_of(v[k], n2, n3) for k in range(r)]
    W = [PEEL.mat_of(w[k], n3, n1) for k in range(r)]

    while not (n1 <= n2 <= n3):
        if n1 > n2:
            U, V, W = [PEEL.transpose(m) for m in U], [PEEL.transpose(m) for m in W], [PEEL.transpose(m) for m in V]
            n1, n2, n3 = n2, n1, n3
        elif n2 > n3:
            U, V, W = [PEEL.transpose(m) for m in W], [PEEL.transpose(m) for m in V], [PEEL.transpose(m) for m in U]
            n1, n2, n3 = n1, n3, n2

    u_flat = [[x for row in U[k] for x in row] for k in range(r)]
    v_flat = [[x for row in V[k] for x in row] for k in range(r)]
    w_flat = [[x for row in W[k] for x in row] for k in range(r)]
    return (n1, n2, n3), u_flat, v_flat, w_flat


def iterated_absorb(fmt, u, v, w, label, pair_order=("uv", "uw", "vw")):
    T = [[list(u[k]), list(v[k]), list(w[k])] for k in range(len(u))]
    PAIR_MAP = {"vw": (1, 2, 0), "uw": (0, 2, 1), "uv": (0, 1, 2)}
    steps = []
    for rnd in range(6):
        changed = False
        for pname in pair_order:
            iy, iz, ix = PAIR_MAP[pname]
            r = len(T)
            Y = [t[iy] for t in T]
            Z = [t[iz] for t in T]
            X = [t[ix] for t in T]
            rk, d, pivs, C = SA.compute_exact_nullspace(Y, Z)
            if d <= 0 or C is None:
                continue
            mk = SA.matroid_maxkill(C, X)
            killed_set = set(mk["killed_terms"])
            if not killed_set:
                continue
            new_X = mk["new_X"]
            newT = []
            for k, t in enumerate(T):
                if k in killed_set:
                    continue
                nt = list(t)
                nt[ix] = new_X[k]
                if any(val != 0 for val in nt[ix]):
                    newT.append(nt)
            print(f"  [{label}] round {rnd} {pname}: r={r} -> {len(newT)} (nullity={d}, killed={len(killed_set)})", flush=True)
            steps.append(f"{pname}:-{len(killed_set)}(null={d})")
            T = newT
            changed = True
        if not changed:
            break
    u2 = [t[0] for t in T]
    v2 = [t[1] for t in T]
    w2 = [t[2] for t in T]
    return u2, v2, w2, steps


def write_vocab_rle(fmt_s, u_s, v_s, w_s, note, out_path):
    def canon(x):
        fr = Fraction(x)
        return int(fr) if fr.denominator == 1 else f"{fr.numerator}/{fr.denominator}"

    U = [[canon(x) for x in r] for r in u_s]
    V = [[canon(x) for x in r] for r in v_s]
    W = [[canon(x) for x in r] for r in w_s]
    vc = Counter(x for m in (U, V, W) for r in m for x in r)
    vocab = [k for k, _ in vc.most_common()]
    v2i = {k: i for i, k in enumerate(vocab)}

    def enc_mat(mat):
        out = []
        for r in mat:
            row_rle = []
            cur, cnt = v2i[r[0]], 1
            for x in r[1:]:
                ix = v2i[x]
                if ix == cur:
                    cnt += 1
                else:
                    row_rle.append(f"{cur}*{cnt}" if cnt > 1 else str(cur))
                    cur, cnt = ix, 1
            row_rle.append(f"{cur}*{cnt}" if cnt > 1 else str(cur))
            out.append(",".join(row_rle))
        return out

    obj = {
        "n": list(fmt_s),
        "m": len(U),
        "ring": "Q",
        "encoding": "vocab_rle_v1",
        "note": note,
        "vocab": vocab,
        "u": enc_mat(U),
        "v": enc_mat(V),
        "w": enc_mat(W),
    }
    raw = json.dumps(obj, separators=(",", ":")) + "\n"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(raw)
    return len(raw), hashlib.sha256(raw.encode("utf-8")).hexdigest()


BEST_SCHEMES = {}


def evaluate_and_record(fmt, u, v, w, note):
    fmt_s, u_s, v_s, w_s = canonicalize_dims(fmt, u, v, w)
    r = len(u_s)
    bars = SOTA_BARS.get(fmt_s, (None, None))
    sota_r, lille_r = bars
    eff_bar = min(sota_r, lille_r) if (sota_r and lille_r) else (sota_r or lille_r)
    s_str = f"{fmt_s[0]}x{fmt_s[1]}x{fmt_s[2]}"

    prev_best = BEST_SCHEMES.get(fmt_s)
    is_new_best = (prev_best is None or r < prev_best[0])
    is_record = (eff_bar is not None and r < eff_bar)

    print(
        f"  [Eval {s_str}] rank={r} | sota={sota_r}, lille_html={lille_r} | "
        f"margin_vs_sota={r - sota_r if sota_r else None}, margin_vs_lille={r - lille_r if lille_r else None} "
        f"{'*** NEW RECORD! ***' if is_record else ''}",
        flush=True,
    )

    if is_record and is_new_best:
        fname = f"{s_str}_r{r}_Q.json"
        out_path = os.path.join(RES_DIR, fname)
        sz, sha = write_vocab_rle(fmt_s, u_s, v_s, w_s, note, out_path)
        ok, msg = VB.verify_file(out_path)
        print(f"  [Verified {fname}] size={sz}B sha256={sha} | {msg}", flush=True)
        assert ok, f"Verification failed on {out_path}: {msg}"
        BEST_SCHEMES[fmt_s] = (r, u_s, v_s, w_s, out_path, sz, sha, note)
    elif is_new_best:
        BEST_SCHEMES[fmt_s] = (r, u_s, v_s, w_s, None, 0, None, note)

    return fmt_s, u_s, v_s, w_s


def peel_best_axis_and_absorb(fmt, u, v, w, parent_label, axes=(0, 1, 2)):
    F = PEEL.Field(None)
    children = {}
    for ax in axes:
        t0 = time.time()
        cen = PEEL.peel_census(fmt, u, v, w, F, ax)
        fmt_p, up, vp, wp = PEEL.project(fmt, u, v, w, F, ax, cen["best_e"], cen["best_f"])
        fmt_ps = tuple(sorted(fmt_p))
        print(
            f"\n-> Peel({parent_label}, ax={ax}) -> {fmt_ps}: raw_peel_rank={len(up)} "
            f"(killed {cen['best_z']} terms, e={cen['best_e']}, f={cen['best_f']}, {time.time()-t0:.1f}s)",
            flush=True,
        )
        u2, v2, w2, st = iterated_absorb(fmt_p, up, vp, wp, f"peel({parent_label},ax={ax})")
        note = (
            f"{fmt_ps[0]}x{fmt_ps[1]}x{fmt_ps[2]} rank {len(u2)} over Q: "
            f"axis-{ax} generalized slice peel of {parent_label} (e={list(cen['best_e'])}, f={list(cen['best_f'])}, -{cen['best_z']} terms)"
            + (f" followed by exact rational nullspace absorption ({','.join(st)})" if st else "")
        )
        fs, us, vs, ws = evaluate_and_record(fmt_p, u2, v2, w2, note)
        if fs not in children or len(us) < len(children[fs][1]):
            children[fs] = (fs, us, vs, ws, f"{fs[0]}x{fs[1]}x{fs[2]}_r{len(us)}")
    return children


def main():
    data_dir = "runs/2026-10-14-0425/data"

    print("=================================================================")
    print("CASCADE 1: LITA 17x17x17_r2723.npz -> 16x17x17 -> 2nd & 3rd Peels")
    print("=================================================================", flush=True)
    fmt17, u17, v17, w17, _ = PEEL.load_scheme(os.path.join(data_dir, "17x17x17_r2723.npz"))
    # Step 1: Peel 17x17x17 along ax=0, 1, 2
    ch1 = peel_best_axis_and_absorb(fmt17, u17, v17, w17, "17x17x17_r2723.npz", axes=(0, 1, 2))

    # Step 2: Peel best (16, 17, 17) along ax=0 (-> 15x17x17) and ax=1, 2 (-> 16x16x17)
    if (16, 17, 17) in ch1:
        f_16_17_17, u_a, v_a, w_a, lbl_a = ch1[(16, 17, 17)]
        ch2 = peel_best_axis_and_absorb(f_16_17_17, u_a, v_a, w_a, lbl_a, axes=(0, 1, 2))

        # Step 3a: Peel (16, 16, 17) along ax=0, 1, 2 (-> 15x16x17 and 16x16x16)
        if (16, 16, 17) in ch2:
            f_16_16_17, u_b, v_b, w_b, lbl_b = ch2[(16, 16, 17)]
            ch3a = peel_best_axis_and_absorb(f_16_16_17, u_b, v_b, w_b, lbl_b, axes=(0, 1, 2))

            # Step 4a: Peel (15, 16, 17) along ax=0, 1, 2 (-> 14x16x17, 15x15x17, 15x16x16)
            if (15, 16, 17) in ch3a:
                f_15_16_17, u_c, v_c, w_c, lbl_c = ch3a[(15, 16, 17)]
                peel_best_axis_and_absorb(f_15_16_17, u_c, v_c, w_c, lbl_c, axes=(0, 1, 2))

        # Step 3b: Peel (15, 17, 17) along ax=0, 1, 2 (-> 14x17x17 and 15x16x17)
        if (15, 17, 17) in ch2:
            f_15_17_17, u_d, v_d, w_d, lbl_d = ch2[(15, 17, 17)]
            ch3b = peel_best_axis_and_absorb(f_15_17_17, u_d, v_d, w_d, lbl_d, axes=(0, 1, 2))
            if (15, 16, 17) in ch3b:
                f_15_16_17b, u_cb, v_cb, w_cb, lbl_cb = ch3b[(15, 16, 17)]
                peel_best_axis_and_absorb(f_15_16_17b, u_cb, v_cb, w_cb, lbl_cb, axes=(0, 1, 2))

    print("\n=================================================================")
    print("CASCADE 2: LITA 18x18x18_r3031.npz -> 17x18x18 -> 2nd & 3rd Peels")
    print("=================================================================", flush=True)
    fmt18, u18, v18, w18, _ = PEEL.load_scheme(os.path.join(data_dir, "18x18x18_r3031.npz"))
    ch18_1 = peel_best_axis_and_absorb(fmt18, u18, v18, w18, "18x18x18_r3031.npz", axes=(0, 1, 2))
    if (17, 18, 18) in ch18_1:
        f_17_18_18, u_e, v_e, w_e, lbl_e = ch18_1[(17, 18, 18)]
        ch18_2 = peel_best_axis_and_absorb(f_17_18_18, u_e, v_e, w_e, lbl_e, axes=(0, 1, 2))
        if (17, 17, 18) in ch18_2:
            f_17_17_18, u_f, v_f, w_f, lbl_f = ch18_2[(17, 17, 18)]
            peel_best_axis_and_absorb(f_17_17_18, u_f, v_f, w_f, lbl_f, axes=(0, 1, 2))

    print("\n=================================================================")
    print("CASCADE 3: LITA 16x16x16_r2236.npz Non-Greedy Axis Peels (ax=1, 2)")
    print("=================================================================", flush=True)
    fmt16, u16, v16, w16, _ = PEEL.load_scheme(os.path.join(data_dir, "16x16x16_r2236.npz"))
    F = PEEL.Field(None)
    for ax in (1, 2):
        cen = PEEL.peel_census(fmt16, u16, v16, w16, F, ax)
        fmt_p, up, vp, wp = PEEL.project(fmt16, u16, v16, w16, F, ax, cen["best_e"], cen["best_f"])
        u2, v2, w2, st = iterated_absorb(fmt_p, up, vp, wp, f"peel(16x16x16_r2236,ax={ax})")
        fs, us, vs, ws = canonicalize_dims(fmt_p, u2, v2, w2)
        print(f"  16x16x16 ax={ax} -> {fs} rank={len(us)}, now peeling to 15x15x16...", flush=True)
        for ax2 in (1, 2):
            cen2 = PEEL.peel_census(fs, us, vs, ws, F, ax2)
            fmt_p2, up2, vp2, wp2 = PEEL.project(fs, us, vs, ws, F, ax2, cen2["best_e"], cen2["best_f"])
            u3, v3, w3, st3 = iterated_absorb(fmt_p2, up2, vp2, wp2, f"peel(15x16x16_from_ax{ax},ax={ax2})")
            evaluate_and_record(fmt_p2, u3, v3, w3, f"2-step peel from 16x16x16_r2236 (ax={ax} then ax={ax2})")

    print("\n=================================================================")
    print("SUMMARY OF ALL RECORD SCHEMES VERIFIED BY verify_brent.py")
    print("=================================================================", flush=True)
    for fmt_s in sorted(BEST_SCHEMES.keys()):
        r, _, _, _, out_path, sz, sha, note = BEST_SCHEMES[fmt_s]
        sota_r, lille_r = SOTA_BARS.get(fmt_s, (None, None))
        if out_path:
            print(
                f"  RECORD {fmt_s[0]}x{fmt_s[1]}x{fmt_s[2]}: rank={r} "
                f"(sota={sota_r} [{r-sota_r}], lille={lille_r} [{r-lille_r}]) | "
                f"file={os.path.basename(out_path)} ({sz}B) | sha256={sha}"
            )
        else:
            print(f"  Non-record best {fmt_s[0]}x{fmt_s[1]}x{fmt_s[2]}: rank={r} (sota={sota_r}, lille={lille_r})")


if __name__ == "__main__":
    main()
