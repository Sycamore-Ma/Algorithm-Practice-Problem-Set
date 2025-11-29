import sys
input = sys.stdin.readline

def lowbit(x):
    return ((x) & (-x))

def bit_add(BIT, x, v):
    n = len(BIT)
    while x < n:
        BIT[x] += v
        x += lowbit(x)

def bit_sum(BIT, x):
    s = 0
    while x > 0:
        s += BIT[x]
        x -= lowbit(x)
    return s


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    ans = []

    # 树状数组单点修改
    for i in range(n):
        BIT = [0] * (n+10)
        cnt = [0] * (n+10)

        # 枚举 mex，树状数组维护大于 mex 的数的个数
        mex = 0
        optimal = None

        for l in range(i, -1, -1):
            ai = a[l]
            if ai <= n:
                bit_add(BIT, ai+1, 1)
                cnt[ai] += 1

                # ai 占领了 mex，需要更新 mex
                if ai == mex:
                    while cnt[mex] > 0 and mex <= n:
                        mex += 1
                # print("l, mex >>>", l, mex)
            
            else:
                # 超出了 n 的排列范围了，一定大于 mex
                bit_add(BIT, n+5, 1)

            seg = i - l + 1
            less_mex = bit_sum(BIT, mex+1)
            weight = seg - less_mex

            if optimal == None or weight > optimal:
                optimal = weight

        # print(">>> optimal:", optimal)
        ans.append(optimal)

    print(*ans)
    # print("ans >>>", *ans)