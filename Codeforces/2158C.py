t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    dp_prefix = [0] * (n + 1)
    dp_surfix = [0] * (n + 1)

    accu = 0
    for i in range(0, n, 1):
        accu = max(accu+a[i], a[i])
        dp_prefix[i] = accu

    accu = 0
    for i in range(n-1, -1, -1):
        accu = max(accu+a[i], a[i])
        dp_surfix[i] = accu

    dp_max_within = [0] * (n + 1)
    ans = -1e18
    for i in range(n):
        dp_max_within[i] = dp_prefix[i] + dp_surfix[i] - a[i]
        if k % 2 == 1:
            # dp_max_within[i] = max(dp_max_within[i] + b[i], dp_max_within[i])
            dp_max_within[i] = dp_max_within[i] + b[i]
        ans = max(ans, dp_max_within[i])

    # print(max(dp_max_within))
    # print(">>>", ans)
    print(ans)