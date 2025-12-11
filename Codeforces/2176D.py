import sys
input = sys.stdin.readline
# import bisect
from bisect import bisect_left


MOD = 998244353

# def

data = list(map(int, sys.stdin.buffer.read().split()))
it = iter(data)
out_lines = []

# t = int(input())
t = next(it)

for _ in range(t):
    # n, m = map(int, input().split())
    # a = list(map(int, input().split()))
    n = next(it)
    m = next(it)
    a = [next(it) for _ in range(n)]

    fr = [0] * (m+10)
    to = [0] * (m+10)
    out_edges = [[] for _ in range(n+10)]

    for edge in range(m):
        # u, v = map(int, input().split())
        u = next(it)
        v = next(it)
        
        u -= 1; v -= 1
        fr[edge] = u
        to[edge] = v
        out_edges[u].append(edge)

    out_vals = [[] for _ in range(n+10)]
    for i in range(n):
        out_edges_i = out_edges[i]
        out_edges_i.sort(key=lambda x: a[to[x]])
        vals = [a[to[e]] for e in out_edges_i]
        out_vals[i] = vals

    dp = [-1] * (m+10)

    def dp_u_to_v(edge):
        if dp[edge] != -1:
            return dp[edge]

        u = fr[edge]
        v = to[edge]
        w = a[u] + a[v]
        # print(">>> edge:", edge, "from", u, "to", v, "a[u]:", a[u], "a[v]:", a[v], "a[u]+a[v]:", w)

        # begin with from u to v, 1 solution
        ans = 1

        out_edges_v = out_edges[v]
        out_vals_v = out_vals[v]

        idx = bisect_left(out_vals_v, w)
        while idx < len(out_edges_v):
            if out_vals_v[idx] != w:
                break
            ans += dp_u_to_v(out_edges_v[idx])
            # ans %= MOD
            if ans >= MOD:
                ans -= MOD
            idx += 1

        dp[edge] = ans
        return ans
    
    ANS = 0
    for edge in range(m):
        ANS += dp_u_to_v(edge)
        # ANS %= MOD
        if ANS >= MOD:
            ANS -= MOD

    # print(ANS)
    # print(">>>", ANS)
    out_lines.append(str(ANS))
    
print('\n'.join(out_lines))