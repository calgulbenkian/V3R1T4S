
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(void) {
    int M, n, d, w;
    if (scanf("%d %d %d %d", &M, &n, &d, &w) != 4) return 2;
    uint64_t *words = (uint64_t *)malloc((size_t)M * sizeof(uint64_t));
    if (!words) return 2;
    for (int i = 0; i < M; i++) {
        unsigned long long x;
        if (scanf("%llu", &x) != 1) return 2;
        words[i] = (uint64_t)x;
    }
    int max_ov = w - d / 2;
    int min_dist = n + 1;
    long long bad_pairs = 0;
    long long hist[65] = {0};
    for (int i = 0; i < M; i++) {
        uint64_t xi = words[i];
        for (int j = i + 1; j < M; j++) {
            int ov = __builtin_popcountll(xi & words[j]);
            int dist = 2 * (w - ov);
            if (dist >= 0 && dist <= 64) hist[dist]++;
            if (dist < min_dist) min_dist = dist;
            if (ov > max_ov) bad_pairs++;
        }
    }
    printf("%d %lld", min_dist, bad_pairs);
    for (int k = 0; k <= n; k++) {
        if (hist[k] > 0) printf(" %d:%lld", k, hist[k]);
    }
    printf("\n");
    free(words);
    return 0;
}
