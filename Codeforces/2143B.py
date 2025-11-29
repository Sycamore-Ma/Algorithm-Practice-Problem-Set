import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort(reverse=True)
    b.sort()
    # print(">>> a", a)
    # print(">>> b", b)

    cost = 0
    cur = 0

    for x in b:
        remains_in_a = n - cur
        if x > remains_in_a:
            continue

        sum_voucher = sum(a[cur:cur+x-1])
        cur += x

        cost += sum_voucher

    if cur < n:
        cost += sum(a[cur:n])

    print(cost)
    # print(">>>", cost)