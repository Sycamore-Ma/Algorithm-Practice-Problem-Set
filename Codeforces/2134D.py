# 柔体
# 把树悬挂起来
# 找到最长的那根绳子作为 a 方向，往下撸
# 找到第一次分叉的地方，作为 b 点
# 找到分叉地方最短的地方，作为 c 点，往下撸


t = int(input())

for _ in range(t):
    n = int(input())

    g = [[] for _ in range(n+1)]
    deg = [0] * (n + 1)

    for _ in range(n-1):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
        deg[u] += 1
        deg[v] += 1

    if all(len(g[i]) <= 2 for i in range(1, n+1)):
        print("-1")
        continue

    # 任选一个分叉点作为根
    root = next(i for i in range(1, n + 1) if deg[i] >= 3)

    near_branch = [-1] * (n + 1)     
    dist_to_branch = [0] * (n + 1)    
    first_from_branch = [-1] * (n + 1)

    def dfs1(u, p, cur_branch, first_hop, dist_from_branch):
        if deg[u] >= 3:
            cur_branch = u
            first_hop = -1   
            dist_from_branch = 0
        near_branch[u] = cur_branch
        dist_to_branch[u] = dist_from_branch
        first_from_branch[u] = first_hop

        for v in g[u]:
            if v == p: continue
            nxt_first = v if deg[u] >= 3 else first_hop
            dfs1(v, u, cur_branch, nxt_first, dist_from_branch + 1)

    dfs1(root, 0, root, -1, 0)

    leaves = [i for i in range(1, n + 1) if deg[i] == 1]

    leaf_star = max(leaves, key=lambda x: dist_to_branch[x])
    b = near_branch[leaf_star]
    p = first_from_branch[leaf_star]

    INF = 10**9
    down = [INF] * (n + 1)
    up   = [INF] * (n + 1)  

    def dfs2(u, p):
        if deg[u] == 1 and u != root:  
            down[u] = 0
        for v in g[u]:
            if v == p: continue
            dfs2(v, u)
            down[u] = min(down[u], down[v] + 1)

    dfs2(root, 0)

    def dfs3(u, p):
        childs = [v for v in g[u] if v != p]
        m = len(childs)
        pref = [INF] * (m + 1)
        suf  = [INF] * (m + 1)
        for i in range(m):
            pref[i+1] = min(pref[i], down[childs[i]] + 1)
        for i in range(m-1, -1, -1):
            suf[i] = min(suf[i+1], down[childs[i]] + 1)
        for i, v in enumerate(childs):
            best_from_u = min(up[u] + 1, pref[i], suf[i+1])  
            up[v] = best_from_u
            dfs3(v, u)

    up[root] = INF
    dist_to_leaf = [0] * (n + 1)
    for i in range(1, n + 1):
        dist_to_leaf[i] = min(down[i], up[i])

    cand = [v for v in g[b] if v != p]
    c = min(cand, key=lambda v: dist_to_leaf[v])

    print(p, b, c)
    # print(">>>", p, b, c)