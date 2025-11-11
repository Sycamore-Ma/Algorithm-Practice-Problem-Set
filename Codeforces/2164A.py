t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())

    maxA = max(a)
    minA = min(a)

    if minA <= x and maxA >= x:
        print("YES")
    else:
        print("NO")