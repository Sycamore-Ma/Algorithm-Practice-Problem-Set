t = int(input())

for _ in range(t):
    n, c = map(int, input().split())
    a = list(map(int, input().split()))

    # a.sort(reverse=True)
    a.sort()

    base = 1

    # 逆序遍历 a

    cost = 0

    for i in range(n-1, -1, -1):
        if a[i] * base > c:
            cost += 1
        else :
            # cost += 0
            base *= 2

    # print(">>>", cost)
    print(cost)