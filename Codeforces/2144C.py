import sys
input = sys.stdin.readline

MOD = 998244353

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    dp_ex = 1
    dp_non = 1

    for i in range(1, n):
        ex_new = 0
        non_new = 0 

        # 上一次没交换 
        if a[i] >= a[i-1] and b[i] >= b[i-1]:   # 这次不交换
            non_new = (non_new + dp_non) % MOD
        if a[i] >= b[i-1] and b[i] >= a[i-1]:   # 这次交换
            ex_new = (ex_new + dp_non) % MOD

        # 上一次交换了
        if a[i] >= b[i-1] and b[i] >= a[i-1]:   # 这次不交换
            non_new = (non_new + dp_ex) % MOD
        if a[i] >= a[i-1] and b[i] >= b[i-1]:   # 这次交换
            ex_new = (ex_new + dp_ex) % MOD

        dp_ex = ex_new
        dp_non = non_new

    ans = (dp_ex + dp_non) % MOD
    print(ans)
    # print(">>>", ans)