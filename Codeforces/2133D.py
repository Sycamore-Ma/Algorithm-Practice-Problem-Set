t = int(input())

for _ in range(t):
    n = int(input())
    h = list(map(int, input().split()))

    dp = [0] * (n+1)
    dp[0] = h[0]
    dp[1] = h[0] + h[1] - 1
    for i in range(2, n):
        kill_previous = dp[i-2] + h[i-1] + max(0, h[i] - i)
        dont_kill_previous = dp[i-1] + h[i] - 1
        dp[i] = min(kill_previous, dont_kill_previous)

    print(dp[n-1])
    # ans = min(dp[n-1], dp[n-2]+h[n-1]-1)
    # print(ans)