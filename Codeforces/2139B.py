t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort(reverse=True)

    ans = 0
    for i in range(n):
        times = m - i
        if times <= 0:
            break
        ans += a[i] * times 

    print(ans)