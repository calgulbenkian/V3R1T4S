#include < algorithm >
#include < cmath >
#include < cstdint >
#include < fstream >
#include < iomanip >
#include < iostream >
#include < numeric >
#include < string >
#include < vector >

constexpr int INF = 1000000000;

struct DeepResult {
    double theta = 0.0;
    double x = 0.0;
    int B = 0;
    int q = 0;
    std::vector< int > M;
};

DeepResult deep_polish(const std::vector< int >& gens, int B_init, int q_init) {
    int B = B_init;
    int q = q_init | 1;
    std::vector<unsigned char> in_mask(B + 1, 0);
    in_mask[0] = 1;
    for (int n = 0; n <= B; ++n) {
        if (in_mask[n]) {
            for (int g : gens) if (n + g <= B) in_mask[n + g] = 1;
        }
    }
    in_mask[B] = 1;

    std::vector< double > xp(2 * B + 2, 1.0);
    std::vector< int > sum_mult(2 * B + 1, 0);
    std::vector< int > kap1(B + 1, INF), cnt1(B + 1, 0), kap2(B + 1, INF), cnt2(B + 1, 0), kap3(B + 1, INF);

    auto optimize_x_and_q = [&](double& cur_x, int& cur_q) -> double {
        std::vector< int > M;
        for (int n = 0; n <= B; ++n) if (in_mask[n]) M.push_back(n);
        std::fill(sum_mult.begin(), sum_mult.end(), 0);
        std::fill(kap1.begin(), kap1.end(), INF);
        kap1[0] = 0;
        for (size_t i = 0; i < M.size(); ++i) {
            int a = M[i];
            sum_mult[2 * a] += 1;
            for (size_t j = 0; j < i; ++j) {
                int b = M[j];
                sum_mult[a + b] += 2;
                if (a + b < kap1[a - b]) kap1[a - b] = a + b;
            }
        }
        auto eval_xq = [&](double x_val, int q_val) {
            xp[0] = 1.0;
            for (int k = 1; k <= 2 * B; ++k) xp[k] = xp[k - 1] * x_val;
            double pp = 0.0;
            for (int s = 0; s <= 2 * B; ++s) if (sum_mult[s] > 0) pp += xp[s];
            double z1 = 1.0;
            int half = (q_val - 1) / 2;
            for (int r = 1; r <= half; ++r) {
                int c = kap1[r];
                if (q_val - r <= B && kap1[q_val - r] < c) c = kap1[q_val - r];
                if (c < INF) z1 += 2.0 * xp[c];
            }
            return 1.0 + std::log(z1 / pp) / std::log((double)q_val);
        };
        double lo = std::exp(-6.8 / B), hi = std::exp(-4.4 / B);
        for (int it = 0; it < 40; ++it) {
            double m1 = lo + (hi - lo) / 3.0;
            double m2 = hi - (hi - lo) / 3.0;
            if (eval_xq(m1, cur_q) < eval_xq(m2, cur_q)) lo = m1;
            else hi = m2;
        }
        cur_x = 0.5 * (lo + hi);
        double best_th = eval_xq(cur_x, cur_q);
        int q_lo = std::max(B + 1, cur_q - 200) | 1;
        int q_hi = std::min(2 * B + 1, cur_q + 200) | 1;
        for (int qt = q_lo; qt <= q_hi; qt += 2) {
            double th = eval_xq(cur_x, qt);
            if (th > best_th) {
                best_th = th;
                cur_q = qt;
            }
        }
        return best_th;
    };

    double cur_x = std::exp(-5.58 / B);
    double cur_th = optimize_x_and_q(cur_x, q);
    std::cout << "Start B=" << B << " q=" << q << " theta=" << cur_th << "\n";

    std::vector< int > touched_r;
    std::vector< int > new_kap_d(B + 1, -1);

    for (int round = 1; round <= 2500; ++round) {
        // Ensure B = max(M)
        while (B > 1 && !in_mask[B]) B--;
        std::vector< int > M;
        for (int n = 0; n <= B; ++n) if (in_mask[n]) M.push_back(n);
        std::fill(sum_mult.begin(), sum_mult.begin() + 2 * B + 1, 0);
        std::fill(kap1.begin(), kap1.begin() + B + 1, INF);
        std::fill(cnt1.begin(), cnt1.begin() + B + 1, 0);
        std::fill(kap2.begin(), kap2.begin() + B + 1, INF);
        std::fill(cnt2.begin(), cnt2.begin() + B + 1, 0);
        std::fill(kap3.begin(), kap3.begin() + B + 1, INF);
        kap1[0] = 0; cnt1[0] = (int)M.size();
        for (size_t i = 0; i < M.size(); ++i) {
            int a = M[i];
            sum_mult[2 * a] += 1;
            for (size_t j = 0; j < i; ++j) {
                int b = M[j];
                int s = a + b, d = a - b;
                sum_mult[s] += 2;
                if (s < kap1[d]) { kap3[d] = kap2[d]; kap2[d] = kap1[d]; cnt2[d] = cnt1[d]; kap1[d] = s; cnt1[d] = 1; }
                else if (s == kap1[d]) { cnt1[d] += 1; }
                else if (s < kap2[d]) { kap3[d] = kap2[d]; kap2[d] = s; cnt2[d] = 1; }
                else if (s == kap2[d]) { cnt2[d] += 1; }
                else if (s < kap3[d]) { kap3[d] = s; }
            }
        }
        xp[0] = 1.0;
        for (int k = 1; k <= 2 * B; ++k) xp[k] = xp[k - 1] * cur_x;
        double pp_base = 0.0;
        for (int s = 0; s <= 2 * B; ++s) if (sum_mult[s] > 0) pp_base += xp[s];
        int half = (q - 1) / 2;
        std::vector< int > c_res(half + 1, INF);
        double z1_base = 1.0;
        for (int r = 1; r <= half; ++r) {
            int c = (r <= B) ? kap1[r] : INF;
            if (q - r <= B && kap1[q - r] < c) c = kap1[q - r];
            c_res[r] = c;
            if (c < INF) z1_base += 2.0 * xp[c];
        }
        cur_th = 1.0 + std::log(z1_base / pp_base) / std::log((double)q);

        double best_round_th = cur_th;
        int best_elem = -1;
        int best_act = 0; // -1 remove, +1 add

        for (int a : M) {
            if (a == 0) continue;
            // Even if a == B, if removing B shrinks B to the previous element < q, that's valid!
            double d_pp = (sum_mult[2 * a] == 1) ? -xp[2 * a] : 0.0;
            touched_r.clear();
            for (int b : M) {
                if (b == a) continue;
                int s = a + b;
                if (sum_mult[s] == 2) d_pp -= xp[s];
                int d = std::abs(a - b);
                if (s == kap1[d] && cnt1[d] == 1) {
                    int other_b = (b < a) ? (a + d) : (a - d);
                    int nk = kap2[d];
                    if (other_b >= 0 && other_b <= B && in_mask[other_b] && a + other_b == kap2[d] && cnt2[d] == 1) {
                        nk = kap3[d];
                    }
                    new_kap_d[d] = nk;
                    int r = (d <= half) ? d : (q - d);
                    if (r >= 1 && r <= half) touched_r.push_back(r);
                }
            }
            std::sort(touched_r.begin(), touched_r.end());
            touched_r.erase(std::unique(touched_r.begin(), touched_r.end()), touched_r.end());
            double d_z1 = 0.0;
            for (int r : touched_r) {
                int k_r = (r <= B) ? ((new_kap_d[r] != -1) ? new_kap_d[r] : kap1[r]) : INF;
                int k_qr = (q - r <= B) ? ((new_kap_d[q - r] != -1) ? new_kap_d[q - r] : kap1[q - r]) : INF;
                int nc = std::min(k_r, k_qr);
                if (nc != c_res[r]) {
                    if (c_res[r] < INF) d_z1 -= 2.0 * xp[c_res[r]];
                    if (nc < INF) d_z1 += 2.0 * xp[nc];
                }
            }
            for (int b : M) {
                if (b != a) new_kap_d[std::abs(a - b)] = -1;
            }
            double th = 1.0 + std::log((z1_base + d_z1) / (pp_base + d_pp)) / std::log((double)q);
            if (th > best_round_th + 1e-13) {
                best_round_th = th;
                best_elem = a;
                best_act = -1;
            }
        }

        if (best_act == 0) {
            std::cout << "Converged at round " << round << ": B=" << B << " q=" << q
                      << " |M|=" << M.size() << " theta=" << cur_th << "\n";
            break;
        }
        in_mask[best_elem] = 0;
        while (B > 1 && !in_mask[B]) B--;
        if (round % 25 == 0) {
            cur_th = optimize_x_and_q(cur_x, q);
            std::cout << "Round " << round << ": B=" << B << " q=" << q
                      << " |M|=" << (M.size() - 1) << " theta=" << cur_th << "\n";
        }
    }
    cur_th = optimize_x_and_q(cur_x, q);
    DeepResult res;
    res.B = B; res.q = q; res.x = cur_x; res.theta = cur_th;
    for (int n = 0; n <= B; ++n) if (in_mask[n]) res.M.push_back(n);
    return res;
}

int main() {
    std::cout << std::setprecision(13);
    DeepResult best;
    std::vector<std::pair<std::vector< int >, std::pair<int, int>>> seeds = {
        {{1518, 1524, 1587, 2024, 2032, 2116}, {19000, 29519}},
        {{3 * 529, 3 * 552, 3 * 554, 4 * 529, 4 * 552, 4 * 554}, {19800, 30295}},
        {{3 * 552, 3 * 576, 3 * 577, 4 * 552, 4 * 576, 4 * 577}, {20600, 32237}},
        {{1971, 2016, 2100, 2628, 2688, 2800}, {26972, 39501}},
    };
    for (auto& s : seeds) {
        auto r = deep_polish(s.first, s.second.first, s.second.second);
        if (r.theta > best.theta) best = r;
    }
    std::cout << "FINAL BEST DEEP POLISHED k=1: B=" << best.B << " q=" << best.q
              << " |M|=" << best.M.size() << " x=" << best.x << " theta=" << best.theta << "\n";
    std::ofstream f("attempts/representation-absorber/deep_k1_cert.json");
    f << "{\n";
    f << "  \"mode\": \"controlled_carry_block_finite\",\n";
    f << "  \"B\": " << best.B << ",\n";
    f << "  \"q\": " << best.q << ",\n";
    f << "  \"k\": 1,\n";
    f << "  \"m\": 1,\n";
    f << "  \"ell\": 10000000000000,\n";
    f << std::setprecision(16) << "  \"x\": \"" << best.x << "\",\n";
    f << "  \"mask\": [";
    for (size_t i = 0; i < best.M.size(); ++i) {
        if (i > 0) f << ", ";
        f << best.M[i];
    }
    f << "]\n}\n";
    return 0;
}
