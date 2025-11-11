import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    # u = []
    # v = []
    # x = []
    # y = []
    
    # 构建有向树
    tree = [[] for _ in range(n+1)]

    for i in range(n-1):
        ui, vi, xi, yi = map(int, input().split())
    #     u.append(ui)
    #     v.append(vi)
    #     x.append(xi)
    #     y.append(yi)



    # for i in range(n-1):
    #     if x[i] > y[i]:
    #         tree[u[i]].append(v[i])
    
        if xi > yi:
            tree[ui].append(vi)
        else:
            tree[vi].append(ui)

    # 拓扑排序
    indeg = [0] * (n+1)
    for i in range(1, n+1):
        for v in tree[i]:
            indeg[v] += 1

    from collections import deque
    q = deque()
    for i in range(1, n+1):
        if indeg[i] == 0:
            q.append(i)

    order = []
    while q:
        node = q.popleft()
        order.append(node)
        for v in tree[node]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    # print(">>> order", order)
    order.reverse()
    # print(">>> reversed order", order)

    ans = [0] * (n+1)
    ansi = 1
    for oi in order:
        ans[oi] = ansi
        ansi += 1

    print(*ans[1:])
    # print(">>>", *ans[1:])