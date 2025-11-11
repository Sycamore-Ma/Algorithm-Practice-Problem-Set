t = int(input())

for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))

    # sum = sum(a)

    # exist_0 = False
    # exist_1 = False
    # exist_2 = False

    cnt_0 = 0
    cnt_1 = 0
    cnt_2 = 0

    for i in range(n):
        if a[i] == 0:
            # exist_0 = True
            cnt_0 += 1
        if a[i] == 1:
            # exist_1 = True
            cnt_1 += 1
        if a[i] == 2:
            # exist_2 = True
            cnt_2 += 1

    sum = cnt_1 + 2 * cnt_2

    ok = True
    ans = []

    if s - sum < 0:
        ans = [0] * cnt_0 + [2] * cnt_2 + [1] * cnt_1
    elif sum == s:
        ok = False    
    elif s - sum == 1:
        # if cnt_1 == 0 or cnt_2 == 0 or cnt_0 == 0:
        #     ok = False
        # else:
        ans = [0] * cnt_0 + [2] * cnt_2 + [1] * cnt_1
    # elif s - sum == 2:
    else:
        ok = False

    if ok:
        print(*ans)
    else:
        print(-1)