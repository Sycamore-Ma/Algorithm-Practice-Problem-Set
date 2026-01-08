import sys
input = sys.stdin.readline
outputs = []

t = int(input())
for _ in range(t):

    n = int(input())
    g = [[] for _ in range(n + 1)]
    for _ in range(n-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)

    # 维护树的 parent / depth
    parent = [0] * n
    depth = [-1] * n
    order = [0]
    depth[0] = 0
    parent[0] = 0

    for u in order:
        for v in g[u]:
            if depth[v] == -1:
                depth[v] = depth[u] + 1
                parent[v] = u
                order.append(v)

    max_depth = max(depth[0:])

    layers = [[] for _ in range(max_depth + 1)]
    for v in range(n):
        layers[depth[v]].append(v)
    
    child_cnt = [0] * n
    for v in range(1, n):
        child_cnt[parent[v]] += 1

    max_layer = max(len(layers[d]) for d in range(max_depth + 1))
    max_child_plus = max(child_cnt[u] + 1 for u in range(n))
    k = max(max_layer, max_child_plus)

    outputs.append(str(k))

# print("==============================")
print("\n".join(outputs))