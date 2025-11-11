import sys
input = sys.stdin.readline

mod = 1000000007
pow2 = [1] * (300 + 10)
for i in range(1, 300 + 10):
    pow2[i] = pow2[i-1] * 2
    pow2[i] %= mod

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # 反例，出现 3 2 1 递减
    # 3 2; 3 1; 2 1 染色冲突

    # dp[i][j] 倒数第二个为 i，最后一个为 j 的方案数
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1


