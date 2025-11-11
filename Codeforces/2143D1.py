import sys
input = sys.stdin.readline

mod = 1000000007
# pow2 = [1] * (300 + 10)
# for i in range(1, 300 + 10):
#     pow2[i] = pow2[i-1] * 2
#     pow2[i] %= mod

t = int(input())
for _ in range(t):
    # n: 1 - 300
    # 300 * 300 * 300 = 27,000,000
    n = int(input())
    a = list(map(int, input().split()))

    # 反例，出现 3 2 1 递减
    # 3 2; 3 1; 2 1 染色冲突

    # dp[i][j] 倒数第二个为 i，最后一个为 j 的方案数
    # dp = [[0] * n for _ in range(n)]
    # for j in range(n):
    #     for i in range(j):
    #         temp = 1
    #         for pre in range(i):
    #             if a[pre] <= a[i]:
    #                 temp += dp[pre][i]
    #                 temp %= mod
    #             elif a[pre] > a[i]:
    #                 if a[pre] <= a[j]:
    #                     temp += dp[pre][i]
    #                     temp %= mod
    #         dp[i][j] = temp

    # print("dp", dp)

    # 统计 3 逆序非法个数更好，用总组合数目减去非法个数

    # dp_good = [[1] * n for _ in range(n)]
    # dp_bad = [[0] * n for _ in range(n)]

    # for j in range(n): # 新追加的位置
    #     for i in range(j): # 倒数第二个位置
    #         for pre in range(i): # 倒数第三个位置
    #             dp_bad[i][j] += dp_bad[pre][i]
    #             dp_bad[i][j] %= mod

    #             if a[pre] > a[i] > a[j]:
    #                 dp_bad[i][j] += dp_good[pre][i]
    #                 dp_bad[i][j] %= mod

                

    #             dp_good[i][j] = pow2[i-1] + mod - dp_bad[i][j]
    #             dp_good[i][j] %= mod

    # print("dp_good", dp_good)
    # print("dp_bad", dp_bad)

    # ans = 0
    # for j in range(n):
    #     for i in range(j):
    #         ans += dp_good[i][j]
    #         ans %= mod


    dp = [[0] * (n+1) for _ in range(n+1)]
    dp[0][0] = 1

    for ai in a:
        # for row in dp:
        #     dp_update = [[0] * (n+1) for _ in range(n+1)]
        dp_update = [row[:] for row in dp]

        # print("dp_update", dp_update)

        # dp[i][j] 非降序双链，分别以 i, j 结尾的方案数

        for i in range(n+1):
            row = dp[i]
            for j in range(i, n+1):
                c = row[j]
                if not c:
                    continue
                if ai >= j:
                    dp_update[i][ai] = (dp_update[i][ai] + c) % mod
                elif ai >= i:   # 对于放在 i j 都满足的，挑选其一就能覆盖。能拆链就是个合法序列
                    dp_update[ai][j] = (dp_update[ai][j] + c) % mod

        dp = dp_update

    ans = 0
    for i in range(n+1):
        for j in range(i, n+1):
            ans += dp[i][j]
            ans %= mod
    
    print(ans)
    # print(">>>", ans)
