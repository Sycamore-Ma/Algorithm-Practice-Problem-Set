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

    ###### 思路不对！
    # 因为阶梯思路并不一定要保证每个阶梯里面都至少贡献一个数字，最后没选上的数字都有可能出现在较后的区间里面，或者窝窝里面

    # print(ans)
    # print(">>>", ans)


    