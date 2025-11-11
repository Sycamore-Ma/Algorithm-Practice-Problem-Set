t = int(input())



for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    prefix_sum = [0] * (n + 1)

    def isOkInterval(day1, day2):
        temp = prefix_sum[day2+1] - prefix_sum[day1]
        return temp <= 0

    for i in range(n+1):
        if i == 0:
            prefix_sum[i] = 0
        else:
            prefix_sum[i] = prefix_sum[i - 1] + a[i - 1]

    startday = 0
    cnt = 0
    while startday < n:
        endday = startday + k - 1
        if endday >= n:
            break
        if isOkInterval(startday, endday):
            cnt += 1
            startday += k+1
        else:
            startday += 1

    print(cnt)
