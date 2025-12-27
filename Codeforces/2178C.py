t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    # X = 0

    # cur = 0
    # nex = 1
    # dp = [0] * (n+10)       # dp[i] 为以 i 为开头的最大

    offset = 0
    best_dp = a[0]      # max(dp[cur] + a[cur])
    max_dp = 0          # max(dp[cur])

    for nex in range(1, n):
        offset -= a[nex]

        dp_nex = best_dp + a[nex]
        if dp_nex > max_dp:
            max_dp = dp_nex

        cand_best_dp = dp_nex + a[nex]
        if cand_best_dp > best_dp:
            best_dp = cand_best_dp

    ans = max_dp + offset
    print(ans)
    # print(">>>", ans)