INF = 0x3f3f3f3f
import heapq

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n)]

    for i in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1

        graph[u].append((v, len(graph[u])))
        graph[v].append((u, len(graph[v])))

    total_time = [INF] * n; total_time[0] = 0
    wait_time = [INF] * n; wait_time[0] = 0
    priority_queue = [(0, 0, 0)]

    while priority_queue:
        total_u, wait_u, u = heapq.heappop(priority_queue)
        if total_u > total_time[u] or total_u == total_time[u] and wait_u > wait_time[u]:   #?
            continue

        deg_u = len(graph[u])
        for v, edge_index in graph[u]:
            target_index = total_u % deg_u + 1 - 1  # 边的索引从 0 开始
            wait_time_here = edge_index - target_index
            wait_time_here = (wait_time_here + deg_u) % deg_u   #?

            total_time_v = total_u + wait_time_here + 1
            wait_time_v = wait_u + wait_time_here

            if total_time_v < total_time[v] or total_time_v == total_time[v] and wait_time_v < wait_time[v]:  #?
                total_time[v] = total_time_v
                wait_time[v] = wait_time_v
                heapq.heappush(priority_queue, (total_time_v, wait_time_v, v))

    print(">>>", total_time[n-1], wait_time[n-1])
