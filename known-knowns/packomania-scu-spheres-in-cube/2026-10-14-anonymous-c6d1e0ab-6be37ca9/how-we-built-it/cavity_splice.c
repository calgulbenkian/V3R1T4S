#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_N 1700
#define M_HIST 12

static double optimal_rescale(int n, double *c, double *out_u) {
    for (int a = 0; a < 3; a++) {
        double mn = 1e30, mx = -1e30;
        for (int i = 0; i < n; i++) {
            double v = c[3 * i + a];
            if (v < mn) mn = v;
            if (v > mx) mx = v;
        }
        double mid = 0.5 * (mn + mx);
        for (int i = 0; i < n; i++) c[3 * i + a] -= mid;
    }
    double max_abs = 0.0;
    for (int k = 0; k < 3 * n; k++) {
        double a = fabs(c[k]);
        if (a > max_abs) max_abs = a;
    }
    if (max_abs < 1e-15) return 0.0;
    double min_d2 = 1e30;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            double dx = c[3 * i] - c[3 * j];
            double dy = c[3 * i + 1] - c[3 * j + 1];
            double dz = c[3 * i + 2] - c[3 * j + 2];
            double d2 = dx * dx + dy * dy + dz * dz;
            if (d2 < min_d2) min_d2 = d2;
        }
    }
    double dmin_u = sqrt(min_d2) / max_abs;
    double r_opt = dmin_u / (2.0 * (2.0 + dmin_u));
    double scale = (0.5 - r_opt) / max_abs;
    for (int k = 0; k < 3 * n; k++) {
        if (out_u) out_u[k] = c[k] / max_abs;
        c[k] *= scale;
    }
    return r_opt;
}

static double eval_fg(int n, const double *c, double R, double *g) {
    int dim = 3 * n;
    for (int k = 0; k < dim; k++) g[k] = 0.0;
    double E = 0.0;
    double twoR = 2.0 * R;
    double twoR2 = twoR * twoR;
    double wall = 0.5 - R;

    for (int i = 0; i < n; i++) {
        for (int a = 0; a < 3; a++) {
            double v = c[3 * i + a];
            if (v > wall) {
                double pen = v - wall;
                E += 0.5 * pen * pen;
                g[3 * i + a] += pen;
            } else if (v < -wall) {
                double pen = -wall - v;
                E += 0.5 * pen * pen;
                g[3 * i + a] -= pen;
            }
        }
        double xi = c[3 * i], yi = c[3 * i + 1], zi = c[3 * i + 2];
        for (int j = i + 1; j < n; j++) {
            double dx = xi - c[3 * j];
            double dy = yi - c[3 * j + 1];
            double dz = zi - c[3 * j + 2];
            double d2 = dx * dx + dy * dy + dz * dz;
            if (d2 < twoR2) {
                double d = sqrt(d2 + 1e-36);
                double pen = twoR - d;
                E += 0.5 * pen * pen;
                double coeff = -pen / d;
                g[3 * i]     += coeff * dx;
                g[3 * i + 1] += coeff * dy;
                g[3 * i + 2] += coeff * dz;
                g[3 * j]     -= coeff * dx;
                g[3 * j + 1] -= coeff * dy;
                g[3 * j + 2] -= coeff * dz;
            }
        }
    }
    return E;
}

static double lbfgs_solve(int n, double *c, double R, int max_iter) {
    int dim = 3 * n;
    static double s_h[M_HIST][3 * MAX_N], y_h[M_HIST][3 * MAX_N], rho[M_HIST], alpha[M_HIST];
    static double g[3 * MAX_N], g_old[3 * MAX_N], c_old[3 * MAX_N], dir[3 * MAX_N], q[3 * MAX_N];

    double E = eval_fg(n, c, R, g);
    int h_cnt = 0, h_head = 0;

    for (int it = 0; it < max_iter; it++) {
        double gn2 = 0.0;
        for (int k = 0; k < dim; k++) gn2 += g[k] * g[k];
        if (E < 1e-31 || gn2 < 1e-31) break;

        for (int k = 0; k < dim; k++) q[k] = g[k];
        for (int m = h_cnt - 1; m >= 0; m--) {
            int idx = (h_head + m) % M_HIST;
            double dot = 0.0;
            for (int k = 0; k < dim; k++) dot += s_h[idx][k] * q[k];
            alpha[m] = rho[idx] * dot;
            for (int k = 0; k < dim; k++) q[k] -= alpha[m] * y_h[idx][k];
        }
        double gamma = 1.0;
        if (h_cnt > 0) {
            int last = (h_head + h_cnt - 1) % M_HIST;
            double sy = 0.0, yy = 0.0;
            for (int k = 0; k < dim; k++) {
                sy += s_h[last][k] * y_h[last][k];
                yy += y_h[last][k] * y_h[last][k];
            }
            if (yy > 1e-32 && sy > 1e-32) gamma = sy / yy;
        }
        for (int k = 0; k < dim; k++) dir[k] = gamma * q[k];
        for (int m = 0; m < h_cnt; m++) {
            int idx = (h_head + m) % M_HIST;
            double dot = 0.0;
            for (int k = 0; k < dim; k++) dot += y_h[idx][k] * dir[k];
            double beta = rho[idx] * dot;
            for (int k = 0; k < dim; k++) dir[k] += s_h[idx][k] * (alpha[m] - beta);
        }
        double dg = 0.0;
        for (int k = 0; k < dim; k++) {
            dir[k] = -dir[k];
            dg += dir[k] * g[k];
        }
        if (dg >= 0.0) {
            for (int k = 0; k < dim; k++) dir[k] = -g[k];
            dg = -gn2;
            h_cnt = 0; h_head = 0;
        }

        memcpy(c_old, c, dim * sizeof(double));
        memcpy(g_old, g, dim * sizeof(double));
        double E_old = E;

        double step = 1.0;
        int ok = 0;
        for (int ls = 0; ls < 20; ls++) {
            for (int k = 0; k < dim; k++) c[k] = c_old[k] + step * dir[k];
            E = eval_fg(n, c, R, g);
            if (E <= E_old + 1e-4 * step * dg) { ok = 1; break; }
            step *= 0.5;
        }
        if (!ok) {
            for (int k = 0; k < dim; k++) c[k] = c_old[k];
            E = E_old;
            break;
        }

        double sy = 0.0;
        for (int k = 0; k < dim; k++) sy += (c[k] - c_old[k]) * (g[k] - g_old[k]);
        if (sy > 1e-30) {
            int slot = (h_head + h_cnt) % M_HIST;
            if (h_cnt == M_HIST) { slot = h_head; h_head = (h_head + 1) % M_HIST; }
            else h_cnt++;
            for (int k = 0; k < dim; k++) {
                s_h[slot][k] = c[k] - c_old[k];
                y_h[slot][k] = g[k] - g_old[k];
            }
            rho[slot] = 1.0 / sy;
        }
    }
    return E;
}

static int load_coords(const char *path, double *c) {
    FILE *f = fopen(path, "r");
    if (!f) return 0;
    int n = 0, idx;
    while (fscanf(f, "%d %lf %lf %lf", &idx, &c[3*n], &c[3*n+1], &c[3*n+2]) == 4) n++;
    fclose(f);
    return n;
}

static void save_u(const char *out_dir, int n, const double *u, double r_opt, const char *method) {
    char path[512];
    snprintf(path, sizeof(path), "%s/scu%d_u.txt", out_dir, n);
    FILE *f = fopen(path, "w");
    if (!f) return;
    fprintf(f, "# N=%d r_opt=%.18g method=%s\n", n, r_opt, method);
    for (int i = 0; i < n; i++) {
        fprintf(f, "%d %.17g %.17g %.17g\n", i + 1, u[3*i], u[3*i+1], u[3*i+2]);
    }
    fclose(f);
}

static void solve_deletion_case(const char *seed_dir, const char *out_dir,
                                int n_target, int n_root, double r_table, double r_aim) {
    char p_root[512];
    snprintf(p_root, sizeof(p_root), "%s/scu%d.txt", seed_dir, n_root);
    static double c_root[3 * MAX_N], c_cur[3 * MAX_N], u_out[3 * MAX_N];
    if (load_coords(p_root, c_root) != n_root) return;

    // Delete (n_root - n_target) spheres from the last indices and relax via L-BFGS
    memcpy(c_cur, c_root, 3 * n_target * sizeof(double));
    lbfgs_solve(n_target, c_cur, r_aim, 2000);
    double r_opt = optimal_rescale(n_target, c_cur, u_out);
    if (r_opt - r_table >= 1e-11) {
        save_u(out_dir, n_target, u_out, r_opt, "deletion_lbfgs_splice");
    }
    printf("[Lens 1: far-import-cavity-splice] N=%4d (from N_root=%4d): r_table=%.18f -> r_opt=%.18f (gain=%+.6e)\n",
           n_target, n_root, r_table, r_opt, r_opt - r_table);
    fflush(stdout);
}

int main(int argc, char **argv) {
    const char *seed_dir = (argc > 1) ? argv[1] : "data/seeds";
    const char *out_dir = (argc > 2) ? argv[2] : "attempts/far-import-cavity-splice/results";

    printf("=== Lens 1 (far-import-cavity-splice): (N+k)-Deletion & Voronoi Cavity Splice + L-BFGS ===\n");
    solve_deletion_case(seed_dir, out_dir, 101, 102, 0.110240604605984488, 0.110240606185);
    solve_deletion_case(seed_dir, out_dir, 466, 469, 0.067898240894769256, 0.067898241055);
    solve_deletion_case(seed_dir, out_dir, 467, 469, 0.067898240894769256, 0.067898241055);
    solve_deletion_case(seed_dir, out_dir, 468, 469, 0.067898240894769256, 0.067898241055);
    solve_deletion_case(seed_dir, out_dir, 793, 796, 0.057356312222008820, 0.057356312362);
    solve_deletion_case(seed_dir, out_dir, 1596, 1688, 0.045385736359615386, 0.045873685242);
    return 0;
}
