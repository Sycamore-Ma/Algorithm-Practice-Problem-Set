t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # 如果从某个 ai 开始出现一段下降，那么 zj 可以取小于 ai 的任何数字，如果 bj 也恰好小于 ai，则一次贡献

    # 数组 a 的下降单调栈
    a_value_stack = []
    a_idx_stack = []

    ans = 0

    for i in range(1, n+1):
        ai = a[i-1]
        bi = b[i-1]

        # 维护下降单调栈，弹出到大于等于 ai 的元素
        while a_value_stack and a_value_stack[-1] < ai:
            a_value_stack.pop()
            a_idx_stack.pop()

        lastIdxGreaterThan_ai = a_idx_stack[-1] if a_idx_stack else 0

        left = 0
        right = len(a_value_stack)-1
        pos = -1
        while left <= right:
            mid = left + right
            mid >>= 1
            if a_value_stack[mid] >= bi:
                pos = mid
                left = mid + 1
            else:
                right = mid - 1

        lastIdxGreaterThan_bi = a_idx_stack[pos] if pos != -1 else 0

        if ai == bi:
            temp = i - lastIdxGreaterThan_ai
        else:
            temp = 0
        temp += min(lastIdxGreaterThan_ai, lastIdxGreaterThan_bi)
        ans += temp * (n-i+1)       # 乘以后面子数组个数

        a_value_stack.append(ai)
        a_idx_stack.append(i)

    print(ans)
    # print(">>>", ans)