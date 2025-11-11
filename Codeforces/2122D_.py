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

    # total_time = [INF] * n; total_time[0] = 0
    # wait_time = [INF] * n; wait_time[0] = 0

    total_time = [[INF] * n for _ in range(n)];   total_time[0][0] = 0
    wait_time = [[INF] * n for _ in range(n)];    wait_time[0][0] = 0

    priority_queue = [(0, 0, 0, 0)]     # 总时间、总等待时间、当前节点、当前时间对准索引

    while priority_queue:
        total_u, wait_u, u, current_index = heapq.heappop(priority_queue)

        # if total_u > total_time[u] or total_u == total_time[u] and wait_u > wait_time[u]:   #?
        #     continue
        if total_u > total_time[u][current_index] or total_u == total_time[u][current_index] and wait_u > wait_time[u][current_index]:   #?
            continue

        deg_u = len(graph[u])
        for v, edge_index in graph[u]:
            # current_index = total_u % deg_u + 1 - 1  # 边的索引从 0 开始
            wait_time_here = edge_index - current_index
            wait_time_here = (wait_time_here + deg_u) % deg_u   #?

            total_time_v = total_u + wait_time_here + 1
            wait_time_v = wait_u + wait_time_here

            deg_v = len(graph[v])
            current_index_v = total_time_v % deg_v + 1 - 1

            # if total_time_v < total_time[v] or total_time_v == total_time[v] and wait_time_v < wait_time[v]:  #?
            #     total_time[v] = total_time_v
            #     wait_time[v] = wait_time_v
            #     heapq.heappush(priority_queue, (total_time_v, wait_time_v, v))

            if total_time_v < total_time[v][current_index_v] or total_time_v == total_time[v][current_index_v] and wait_time_v < wait_time[v][current_index_v]:  #?
                total_time[v][current_index_v] = total_time_v
                wait_time[v][current_index_v] = wait_time_v
                heapq.heappush(priority_queue, (total_time_v, wait_time_v, v, current_index_v))


    # print(">>>", total_time[n-1], wait_time[n-1])

    # 换行打印矩阵
    for row in total_time:
        print(row)
    for row in wait_time:
        print(row)

    min_total_time = INF
    min_wait_time = INF
    for i in range(n):
        if total_time[n-1][i] < min_total_time or total_time[n-1][i] == min_total_time and wait_time[n-1][i] < min_wait_time:
            min_total_time = total_time[n-1][i]
            min_wait_time = wait_time[n-1][i]

    print(">>>", min_total_time, min_wait_time)