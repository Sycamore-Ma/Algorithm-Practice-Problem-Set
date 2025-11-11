import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    ans = 0

    edges = [[] for __ in range(n+1)]
    degrees = [0] * (n+1)

    for i in range(n-1):
        u, v = map(int, input().split())
        edges[u].append(v)
        edges[v].append(u)
        degrees[u] += 1
        degrees[v] += 1

    if n <= 2:
        ans = 0
    else:
        max_cnt = 0
        leef_cnt = 0
        for choose_as_root in range(1, n+1):
            
            if degrees[choose_as_root] == 1:
                leef_cnt += 1

            cnt = 0
            for neighbor in edges[choose_as_root]:
                if degrees[neighbor] == 1:
                    cnt += 1
            max_cnt = max(max_cnt, cnt)
        
        

        ans = leef_cnt - max_cnt

    print(ans)
    # print(">>>", ans)
            