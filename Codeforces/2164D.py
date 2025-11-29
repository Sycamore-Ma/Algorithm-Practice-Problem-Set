import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, kmax = map(int, input().split())
    print(">>> n, kmax:", n, kmax)
    s = input().strip()
    t = input().strip()
    # s = list(input().strip())
    # t = list(input().strip())
    s = list(s)
    t = list(t)
    print(">>> s, t:", "".join(s), "".join(t))

    if s[0] != t[0]:
        print("-1")
        continue

    lastSeen = [-1] * 26
    lastPos = [-1] * n
    ok = True
    step = 0

    for i in range(n):
        lastSeen[ord(s[i]) - ord('a')] = i
        pos = lastSeen[ord(t[i]) - ord('a')]

        if pos == -1:
            ok = False
            break

        lastPos[i] = pos
        stepi = i - pos
        if stepi > step:
            step = stepi
        if step > kmax:
            ok = False
            break

    if not ok:
        print("-1")
        continue

    targetPos = list(range(n))
    for i, pos in enumerate(lastPos):
        if pos > i:
            ok = False
            break
        if pos >= 0:
            if i > targetPos[pos]:
                targetPos[pos] = i

    if not ok:
        print("-1")
        continue

    cur = s[:]
    ans = []

    for _ in range(step):
        print(">>> targetPos:", targetPos)
        s_prime = cur[:]
        newTargetPos = targetPos[:]
        for i in range(n-1):
            if targetPos[i] > i:
                s_prime[i+1] = cur[i]
            newTargetPos[i+1] = targetPos[i]
        ans.append("".join(s_prime))
        cur = s_prime
        targetPos = newTargetPos
        print(">>> cur:", "".join(cur))

    print("=======================================")
    print("".join(s), "".join(t))
    print("targetPos:", targetPos)
    print(str(len(ans)))
    print("\n".join(ans))
    print("=======================================")
