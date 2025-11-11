t = int(input())

for _ in range(t):
    n = int(input())
    g = list(map(int, input().split()))

    # g.sort(reverse=True)
    g.sort()

    ans = 0

    for i in range(n-1, -1, -2):
        # print("--", i)
        ans += g[i]

    print(ans)
    # print(">>>", ans)

