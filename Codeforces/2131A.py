t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    cnt_a_greater_b = 0

    for i in range(n):
        if a[i] > b[i]:
            cnt_a_greater_b += a[i] - b[i]

    print(cnt_a_greater_b+1)
    # print(">>>", cnt_a_greater_b+1)
