# 两侧金字塔阶梯，直到首次出现最大值 max_h，中间可以有窝窝
# 中间窝窝里面的区间随便选，选法为 2 的幂次
# 乘上左边选法
# 乘上右边选法

import sys
input = sys.stdin.readline

MOD = 998244353

POW2 = [1] * (5000 + 10)
for i in range(1, 5000 + 10):
    POW2[i] = (POW2[i-1] * 2) % MOD

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    max_h = max(a)

    stair_left = []
    stair_right = []

    # inner_left_pos = -1
    # inner_right_pos = -1

    stair_left_pos = []
    stair_right_pos = []

    for i in range(n):
        if i == 0:
            stair_left.append(a[i])
            # inner_left_pos = 0
            stair_left_pos.append(i)
        else:
            if a[i] > stair_left[-1]:
                stair_left.append(a[i])
                # inner_left_pos = i
                stair_left_pos.append(i)
        # print(">>>", i, stair_left, inner_left_pos)

    for i in range(n-1, -1, -1):
        if i == n-1:
            stair_right.append(a[i])
            # inner_right_pos = n-1
            stair_right_pos.append(i)
        else:
            if a[i] > stair_right[-1]:
                stair_right.append(a[i])
                # inner_right_pos = i
                stair_right_pos.append(i)
        # print(">>>", i, stair_right, inner_right_pos)

    stair_right.reverse()
    stair_right_pos.reverse()

    # print("stair_left", stair_left)
    # print("stair_right", stair_right)
    # # print("inner_left_pos", inner_left_pos)
    # # print("inner_right_pos", inner_right_pos)
    # print("stair_left_pos", stair_left_pos)
    # print("stair_right_pos", stair_right_pos)

    max_pos = [i for i in range(n) if a[i] == max_h]

    # helper: count waysL(p)
    def waysL(p):
        # 统计 [0..p] 区间
        res = 1
        prev = 0
        for idx, val in zip(stair_left_pos, stair_left):
            if idx > p:  # 只考虑到 p 为止
                break
            # 本层范围是 [prev..idx] inclusive
            low_cnt = 0
            equal_cnt = 0
            for j in range(prev, idx+1):
                if a[j] < val:
                    low_cnt += 1
                elif a[j] == val:
                    equal_cnt += 1
            if val == max_h and idx == p:
                # 必须包含位置 p 这个最大值
                equal_cnt -= 1
                if equal_cnt < 0:
                    return 0
                res = res * POW2[low_cnt] % MOD
                res = res * POW2[equal_cnt] % MOD
            else:
                res = res * POW2[low_cnt] % MOD
                res = res * (POW2[equal_cnt] - 1) % MOD
            prev = idx+1
        return res % MOD

    # helper: count waysR(q)
    def waysR(q):
        res = 1
        prev = n-1
        for idx, val in zip(reversed(stair_right_pos), reversed(stair_right)):
            if idx < q:
                break
            low_cnt = 0
            equal_cnt = 0
            for j in range(idx, prev+1):
                if a[j] < val:
                    low_cnt += 1
                elif a[j] == val:
                    equal_cnt += 1
            if val == max_h and idx == q:
                equal_cnt -= 1
                if equal_cnt < 0:
                    return 0
                res = res * POW2[low_cnt] % MOD
                res = res * POW2[equal_cnt] % MOD
            else:
                res = res * POW2[low_cnt] % MOD
                res = res * (POW2[equal_cnt] - 1) % MOD
            prev = idx-1
        return res % MOD

    # ---- 枚举所有 (p,q) ----
    ans = 0
    for p in max_pos:
        wL = waysL(p)
        if wL == 0:
            continue
        for q in max_pos:
            if q < p:
                continue
            wR = waysR(q)
            if wR == 0:
                continue
            mid = q - p - 1
            if mid < 0:
                mid_pow = 1
            else:
                mid_pow = POW2[mid]
            ans = (ans + wL * wR % MOD * mid_pow) % MOD

    print(ans)
    print(">>>", ans)