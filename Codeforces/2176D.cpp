#include <bits/stdc++.h>
using namespace std;
#define ll long long

const ll MOD = 998244353;

vector<ll> a;
vector<int> fr, to;
vector<vector<int>> out_edges;
vector<vector<ll>> out_vals;
vector<ll> dp;

// ll dp_u_to_v(int edge) {
//     if (dp[edge] != -1) return dp[edge];

//     int u = fr[edge];
//     int v = to[edge];
//     ll w = a[u] + a[v];

//     // cout << "u:" << u << " v:" << v << "\t";
//     // cout << "a[u]" << a[u] << " a[v]:" << a[v] << "\t";
//     // cout << "a[u] + a[v]:" << w << "\n";

//     ll ans = 1;

//     auto &out_edges_v = out_edges[v];
//     auto &out_vals_v  = out_vals[v];

//     int idx = (int)(lower_bound(out_vals_v.begin(), out_vals_v.end(), w) - out_vals_v.begin());
//     while (idx < (int)out_edges_v.size()) {
//         if (out_vals_v[idx] != w) break;
//         ans += dp_u_to_v(out_edges_v[idx]);
//         if (ans >= MOD) ans -= MOD;
//         ++idx;
//     }

//     dp[edge] = ans;
//     return ans;
// }

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (!(cin >> t))    return 0;

    while (t --) {
        int n, m;
        cin >> n >> m;

        a.assign(n, 0);
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }

        fr.assign(m + 10, 0);
        to.assign(m + 10, 0);
        // out_edges.assign(n + 10, {});
        // out_vals.assign(n + 10, {});
        dp.assign(m + 10, -1);

        for (int edge = 0; edge < m; ++edge) {
            int u, v;
            cin >> u >> v;
            --u;    --v;
            fr[edge] = u;
            to[edge] = v;
            // out_edges[u].push_back(edge);
        }

        // out_edges[i].sort(key=lambda x: a[to[x]])
        // out_vals[i] = [a[to[e]] for e in out_edges_i]
        // for (int i = 0; i < n; ++i) {
        //     auto &out_edges_i = out_edges[i];
        //     sort(out_edges_i.begin(), out_edges_i.end(),
        //          [&](int x, int y) { return a[to[x]] < a[to[y]]; });

        //     auto &vals = out_vals[i];
        //     vals.reserve(out_edges_i.size());
        //     for (int e : out_edges_i) {
        //         vals.push_back(a[to[e]]);
        //     }
        // }

        // ll ANS = 0;
        // for (int edge = 0; edge < m; ++edge) {
        //     ANS += dp_u_to_v(edge);
        //     if (ANS >= MOD)     ANS -= MOD;
        // }

        // cout << ANS << '\n';

        vector<int> ord(m);
        iota(ord.begin(), ord.end(), 0);
        sort(ord.begin(), ord.end(), [&](int e1, int e2) {
            if (a[to[e1]] != a[to[e2]]) return a[to[e1]] > a[to[e2]];
            return fr[e1] < fr[e2];
        });


    }

    return 0;
}