import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, y = map(int, input().split())
    c = list(map(int, input().split()))

    c_max = max(c)
    cnt = [0] * (c_max + 10)
    for ci in c:
        cnt[ci] += 1

    prefix_cnt = [0] * (c_max + 10)
    for i in range(1, c_max + 10):
        prefix_cnt[i] = prefix_cnt[i-1] + cnt[i]

    INF = 10**30
    ans = -INF


    for x in range(2, c_max + 2):   # 枚举打折折扣，分母到 c_max+1，再往后就没意义了
        tot_price = 0
        reused_cnt = 0
        new_c_max = (c_max+x-1) // x    # c_max / x 向上取整
        
        for ci in range(1, new_c_max + 1):  # 枚举打折后的新价格桶
            left = (ci-1) * x + 1           # 映射的旧价格区间左端点
            right = min(ci * x, c_max)      # 映射的旧价格区间右端点

            if left > c_max:
                break

            new_cnt = prefix_cnt[right] - prefix_cnt[left-1]
            if new_cnt == 0:
                continue

            tot_price += new_cnt * ci
            old_tag_cnt = cnt[ci]
            reused_cnt += min(old_tag_cnt, new_cnt)

        
        tot_price -= (n - reused_cnt) * y
        if tot_price > ans:
            ans = tot_price

    print(ans)
    # print(">>>", ans)


"""
4
5 51
50 150 50 148 150
3 1000000000
42 42 42
10 54321
1 8088 45 1 73 1 9198 4991 1 83
3 100
1 1 1
"""


# C/x 的 sigma_x(C/x) = O(C log C)