# 每次：
# 1 查询重心
# 2 切掉重心
# 这样切得少，查到最后就不用切太多

t = int(input())


# def init_build(cur, cur_par):
    

# def get_center(cur, cur_par):


import sys
sys.setrecursionlimit(1 << 18)



for _ in range(t):
    n = int(input())
    g = [[] for _ in range(n+1)]
    par = [0] * (n+1)
    size = [0] * (n+1)
    visited = []
    operations = []


    # def build_tree(cur, cur_par):
    #     par[cur] = cur_par
    #     size[cur] = 1
    #     visited.append(cur)

    #     for v in g[cur]:
    #         if v != cur_par:
    #             build_tree(v, cur)
    #             size[cur] += size[v]


    def build_tree(cur, cur_par):
        # visited.clear()
        par[cur] = cur_par
        stack = [cur]
        while stack:
            u = stack.pop()
            visited.append(u)
            for v in g[u]:
                if v == par[u]:
                    continue
                par[v] = u
                stack.append(v)
        for u in visited:
            size[u] = 0
        for u in reversed(visited):
            s = 1
            for v in g[u]:
                if v == par[u]:
                    continue
                s += size[v]
            size[u] = s


    def get_center(cur, cur_par):
        visited.clear()
        build_tree(cur, cur_par)

        total_size = size[cur]
        center = cur
        opt_val = total_size + 1000000

        for u in visited:
            max_part = total_size - size[u]
            for v in g[u]:
                if v != par[u]:
                    if size[v] > max_part:
                        max_part = size[v]
            if max_part < opt_val:
                opt_val = max_part
                center = u

        theLastOne = False
        if total_size == 1:
            theLastOne = True

        return center, theLastOne



    for i in range(n-1):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    
    if n == 2:
        print(2)
        print(1, 1)
        print(1, 2)
        continue

    if n == 3:
        print(3)
        print(1, 1)
        print(1, 2)
        print(1, 3)
        continue

    dfs_visited = [False] * (n+1)

    def dfs(cur, cur_par):

        center, theLastOne = get_center(cur, cur_par)
        # dfs_visited[center] = True

        if theLastOne:
            operations.append((1, center))
            return 
        else:
            operations.append((1, center))
            operations.append((2, center))

        # for v in g[center]:
        #     if v != cur_par:
        #         dfs(v, center)
        #     # if not dfs_visited[v]:
        #     #     dfs_visited[v] = True
        #     #     dfs(v, center)

        in_block = [False] * (n+1)
        for u in visited:
            in_block[u] = True

        for v in g[center]:
            if not in_block[v]:
                continue
            dfs(v, center)


    dfs(1, 0)

    print(len(operations))
    for op in operations:
        print(*op)