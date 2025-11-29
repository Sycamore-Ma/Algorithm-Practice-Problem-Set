t = int(input())

# 找循环节


def cal_MEX(a, n):
    cnt = [0] * (n + 1)
    for ai in a:
        if ai <= n:
            cnt[ai] += 1

    MEX = 0
    while MEX <= n and cnt[MEX] > 0:
        MEX += 1

    a_new = [0] * n
    for i in range(n):
        ai = a[i]
        if ai < MEX and cnt[ai] == 1:
            a_new[i] = ai
        else:
            a_new[i] = MEX
    return a_new

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    visited = {}
    states = []

    i = 0
    while i < k:
        static_a = tuple(a)
        if static_a in visited:
            bg = visited[static_a]
            cycle_len = len(states) - bg
            idx = bg + (k - bg) % cycle_len
            a = list(states[idx])
            break
        visited[static_a] = len(states)
        states.append(static_a)
        a = cal_MEX(a, n)
        i += 1

    ans = sum(a)
    print(ans)
    # print(">>>", ans)