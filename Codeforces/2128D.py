t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    # 只会上升一个越界，不可能同时比【左边】和【左边的左边】更大
    # 7 5 1 6 X
    # 7 5 1 4 V

    # 把谷值去掉，下降的对儿就是区间内 LDS 长度
    # 7 5 1 4 3 V

    LDS = 0

    for i in range(0, n-1):
        if p[i] > p[i+1]:
            # l 有 i+1 种选法，r 有 n-i-1 种选法
            LDS += (i+1) * (n-i-1)

    # 每个独立元素也算
    LDS += n    
    # 独立元素之外的每个数组其中的对儿数目需要加一，1 2 3 为两对，1 2 3 4 为四对，即为 C(n, 2)
    LDS += n * (n-1) // 2

    print(LDS)
