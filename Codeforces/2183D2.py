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

    color = [0] * n
    color[0] = 1

    # helper: per-layer "DSU in dict" to pick smallest unused color
    # find(x): smallest >= x not used in this layer
    def layer_assign(nodes):
        used_next = {}  # DSU mapping only for colors used in this layer

        def find(x):
            while x <= k and x in used_next:
                used_next[x] = used_next.get(used_next[x], used_next[x])
                x = used_next[x]
            return x if x <= k else k + 1

        def use(c):
            used_next[c] = find(c + 1)

        assigned = []  # nodes already assigned in this layer, for possible swap

        m = len(nodes)
        if m == 0:
            return

        # assign all but last greedily
        for v in nodes[:-1]:
            ban = color[parent[v]]  # parent's color
            c = find(1)
            if c == ban:
                c2 = find(ban + 1)
                if c2 <= k:
                    c = c2
                else:
                    # This situation should not happen here (only possible at the last node).
                    # But keep it safe: pick a color < ban if exists (ban is smallest remaining).
                    # If c==ban and no >ban exists => only ban remains, impossible for non-last.
                    pass
            color[v] = c
            use(c)
            assigned.append(v)

        # last node
        v = nodes[-1]
        ban = color[parent[v]]
        c = find(1)
        if c != ban and c <= k:
            color[v] = c
            use(c)
            return

        c2 = find(ban + 1)
        if c2 <= k:
            color[v] = c2
            use(c2)
            return

        # swap case: only color left is ban, need swap with someone whose ban != ban
        # since ban appears at most k-1 times among this layer (children constraint), such node exists when m==k
        swap_u = None
        for u in assigned:
            if color[parent[u]] != ban:
                swap_u = u
                break
        # must exist
        # v takes u's color, u takes ban
        color[v] = color[swap_u]
        color[swap_u] = ban
        # (no need to update DSU, we still used all m colors in this layer)

    # process layers from depth 1..max_depth
    for d in range(1, max_depth + 1):
        layer_assign(layers[d])

    # build operations by color classes
    buckets = [[] for _ in range(k + 1)]
    for v in range(n):
        buckets[color[v]].append(v)

    outputs.append(str(k))
    for c in range(1, k + 1):
        nodes = buckets[c]
        nodes = [v + 1 for v in nodes]
        if nodes:
            outputs.append(str(len(nodes)) + " " + " ".join(map(str, nodes)))
        else:
            outputs.append("0")

# print("==============================")
print("\n".join(outputs))