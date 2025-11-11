t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    left_greater = [0] * n
    right_greater = [0] * n
    # option = [-1] * n
    a = [0] * n

    for i in range(n):
        for j in range(i + 1, n):
            if p[i] > p[j]:
                left_greater[j] += 1
            if p[i] < p[j]:
                right_greater[i] += 1

    # print("left ===", left_greater)
    # print("right ===", right_greater)

    for i in range(n):
        if left_greater[i] <= right_greater[i]:
            # option[i] = 0
            a[i] = p[i]
        elif left_greater[i] > right_greater[i]:
            # option[i] = 1
            a[i] = n*2-p[i]
    # print("option ===", option)
    # print("a ===", a)
    # print(">>>", sum(option))
    # print(sum(option))

    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                ans += 1

    # print(">>>", ans)
    print(ans)
    