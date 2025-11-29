import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    SUM = 0
    for i in range(n):
        if i % 2 == 0:
            SUM += a[i]
        else:
            SUM -= a[i]

    cost = 0

    # 同奇偶替换
    if n == 1:
        cost = 0
    else:
        cost = (n - 1) if (n % 2 == 1) else (n - 2)


    # 异奇偶替换
    INF = 10**16
    min_odd = INF
    
    for j in range(n):
        x = a[j]
        if j % 2 == 1:
            if min_odd < INF:
                cand = (2 * x + j + 1) - min_odd
                if cand > cost:
                    cost = cand
        else:
            val = 2 * x + j + 1
            if val < min_odd:
                min_odd = val

    # 异偶奇替换
    min_even = INF

    for j in range(n):
        x = a[j]
        if j % 2 == 0:
            if min_even < INF:
                cand = (-2 * x + j + 1) - min_even
                if cand > cost:
                    cost = cand
        else:
            val = -2 * x + j + 1
            if val < min_even:
                min_even = val

    ans = SUM + max(0, cost)
    print(ans)



# 同奇偶交换只增加 cost
# 异奇偶交换增加 cost + gain
# ALICE 会挑选一个最大贡献对儿
# BOB 会在第一次立刻结束，因为他做完也会被 Alice 拉回来，而且多了一个 cost