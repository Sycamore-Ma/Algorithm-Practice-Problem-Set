import sys
input = sys.stdin.readline

t = int(input())

import heapq

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    a.sort()
    enemy = sorted([(b[i], c[i]) for i in range(m)])

    ans = 0
    enemyIdx = 0

    swordHeap = []
    enemyHeap = []

    for ai in a:
        heapq.heappush(swordHeap, ai)

    while swordHeap:
        s = heapq.heappop(swordHeap)

        while enemyIdx < m and enemy[enemyIdx][0] <= s:
            bval, cval = enemy[enemyIdx]
            heapq.heappush(enemyHeap, (-cval, bval))
            enemyIdx += 1

        if not enemyHeap:   # 垃圾刀
            continue

        cval = -enemyHeap[0][0]
        bval = enemyHeap[0][1]
        heapq.heappop(enemyHeap)
        ans += 1

        if cval > 0:
            s_new = max(s, cval)
            # while enemyIdx < m and enemy[enemyIdx][0] <= s_new:
            #     bnext, cnext = enemy[enemyIdx]
            #     heapq.heappush(enemyHeap, (-cnext, bnext))
            #     enemyIdx += 1
            heapq.heappush(swordHeap, s_new)
        else:
            continue    # 浪费了一个最低的刀

    print(ans)
    # print(">>>", ans)