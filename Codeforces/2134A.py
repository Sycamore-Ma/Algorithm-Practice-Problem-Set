t = int(input())

for _ in range(t):
    n, a, b = map(int, input().split())

    OK = True

    sub = max(0, a-b)

    if sub % 2 == 1: # 红色不对称
        OK = False

    if n % 2 == 0:
        if b % 2 == 1:  # 蓝色不对称
            OK = False
    else :
        if b % 2 == 0:
            OK = False

    print("YES" if OK else "NO")
