t = int(input())

for _ in range(t):
    n = int(input())

    ans = 0

    for i in range(n):
        a, b, c, d = map(int, input().split())
        if a == c and b == d:
            continue

        if a > c:
            ans += a - c

        if b > d:
            ans += (b - d) + min(a, c)

    # print(">>>", ans)
    print(ans)