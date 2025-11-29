t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    # 1 1 1 5 5
    # 1 2 2 4
    # 1 2 3 3 5

    ok = True

    for i, ai in enumerate(a):
        if i == 0:
            continue
        if i % 2 == 0:
            if a[i] != a[i-1]:
                ok = False
                break
    if ok:
        print("YES")
    else:
        print("NO")