import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    counter = [0] * (m+1)
    sets = []

    for __ in range(n):
        # l = int(input())
        s = list(map(int, input().split()))
        sets.append(s)

        # for si in s:
        #     counter[si] += 1
        for i in range(1, s[0]+1):
            si = s[i]
            counter[si] += 1

    OK = True
    for si in range(1, m+1):
        if counter[si] == 0:
            OK = False
            break

    # print("counter >>>", counter)
    # print(sets)
    # print("OK >>>", OK)

    uselessSetsCnt = 0
    for s in sets:
        ok = True
        # for si in s:
        for i in range(1, s[0]+1):
            si = s[i]
            if counter[si] < 2:
                ok = False
                break
        if ok:
            uselessSetsCnt += 1

    if uselessSetsCnt < 2:
        OK = False

    if OK:
        print("YES")
    else:
        print("NO")