#!/usr/bin/env python3
"""make_all_remaining_results.py -- Convert and verify the 5 remaining FMM record schemes (< 1 MB each)."""
import hashlib, json, math, os, subprocess, sys
from collections import Counter
from fractions import Fraction

def primitive_int_vec(vec):
    lcm_d = 1
    for x in vec:
        if x != 0:
            lcm_d = math.lcm(lcm_d, x.denominator)
    iv = [int(x * lcm_d) for x in vec]
    g = 0
    for x in iv:
        if x != 0:
            g = math.gcd(g, abs(x))
    first_nz = next(x for x in iv if x != 0)
    if first_nz < 0:
        g = -g
    iv = [x // g for x in iv]
    return iv, Fraction(g, lcm_d)

def to_sparse_flat(vec):
    out = []
    for idx, val in enumerate(vec):
        if val != 0:
            out.append(idx)
            if isinstance(val, int) or val.denominator == 1:
                out.append(int(val))
            else:
                out.append(f"{val.numerator}/{val.denominator}")
    return out

def convert_sparse_flat(in_path, out_path, note):
    with open(in_path, "r", encoding="utf-8") as f:
        d = json.load(f)
    u_out, v_out, w_out = [], [], []
    for uk, vk, wk in zip(d["u"], d["v"], d["w"]):
        uf = [Fraction(x) for x in uk]
        vf = [Fraction(x) for x in vk]
        wf = [Fraction(x) for x in wk]
        ui, su = primitive_int_vec(uf)
        vi, sv = primitive_int_vec(vf)
        ws = [x * su * sv for x in wf]
        u_out.append(to_sparse_flat(ui))
        v_out.append(to_sparse_flat(vi))
        w_out.append(to_sparse_flat(ws))
    obj = {
        "n": d["n"],
        "m": len(u_out),
        "ring": "Q",
        "encoding": "sparse_flat_pairs",
        "note": note,
        "u": u_out,
        "v": v_out,
        "w": w_out,
    }
    raw = json.dumps(obj, separators=(",", ":")) + "\n"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(raw)
    return len(raw), hashlib.sha256(raw.encode("utf-8")).hexdigest()

def convert_vocab_rle(in_path, out_path, note):
    with open(in_path, "r", encoding="utf-8") as f:
        d = json.load(f)
    # Normalize each entry string canonically via Fraction
    def canon(x):
        fr = Fraction(x)
        return int(fr) if fr.denominator == 1 else f"{fr.numerator}/{fr.denominator}"
    U = [[canon(x) for x in r] for r in d["u"]]
    V = [[canon(x) for x in r] for r in d["v"]]
    W = [[canon(x) for x in r] for r in d["w"]]
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
        "n": d["n"],
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

def main():
    cand_dir = "runs/2026-10-14-0004/attempts/representation-absorber/candidates"
    res_dir = "runs/2026-10-14-0004/attempts/representation-absorber/result"
    os.makedirs(res_dir, exist_ok=True)
    jobs = [
        ("13x13x14_r1499_Q_from1541_ax1.json", "13x13x14_r1499_Q.json", "sparse",
         "13x13x14 rank 1499 over Q: axis-1 slice peel of 13x14x14_r1541_Q.json (-29 terms) followed by exact 7-dimensional uw-nullspace matroid max-kill (-13 terms)."),
        ("13x14x15_r1646_Q_from_13x15x15_r1763_ax2.json", "13x14x15_r1646_Q.json", "sparse",
         "13x14x15 rank 1646 over Q: axis-2 generalised slice peel (-117 terms) of 13x15x15_r1763_Q.json."),
        ("13x14x14_r1541_Q_from1646_ax2.json", "13x14x14_r1541_Q.json", "sparse",
         "13x14x14 rank 1541 over Q: axis-2 generalised slice peel (-105 terms) of 13x14x15_r1646_Q.json."),
        ("14x14x15_r1715_Q_abs.json", "14x14x15_r1715_Q.json", "sparse",
         "14x14x15 rank 1715 over Q: exact 1-dimensional uw-nullspace absorption (-1 term) on 14x14x15_r1716_Q.json."),
        ("14x16x16_r2119_Q_from2180_ax0.json", "14x16x16_r2119_Q.json", "vrle",
         "14x16x16 rank 2119 over Q: axis-0 slice peel (-41 terms) of 15x16x16_r2180_Q.json followed by 9D vw-nullspace hub max-kill (-19 terms) and 1D uv-nullspace absorption (-1 term)."),
    ]
    for src, dst, mode, note in jobs:
        in_p = os.path.join(cand_dir, src)
        out_p = os.path.join(res_dir, dst)
        if mode == "sparse":
            sz, sha = convert_sparse_flat(in_p, out_p, note)
        else:
            sz, sha = convert_vocab_rle(in_p, out_p, note)
        r = subprocess.run([sys.executable, "runs/2026-10-14-0004/verify_brent.py", out_p],
                           capture_output=True, text=True, check=True)
        print(f"{dst}: size={sz}B sha256={sha} | {r.stdout.strip()}")

if __name__ == "__main__":
    main()
