import sys
from bisect import bisect_right
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = input().strip()
    b = input().strip()

    aPreSum = [0]*(n+1)
    bPreSum = [0]*(n+1)
    for i in range(1, n+1):
        aPreSum[i] = aPreSum[i-1] + (a[i-1] == '1')
        bPreSum[i] = bPreSum[i-1] + (b[i-1] == '1')

    arr = []
    for y in range(1, n+1):
        By = bPreSum[y]
        dy = 2*By - y
        zy = y - By
        arr.append((dy, By, zy))

    arr.sort(key=lambda x: x[0])
    d_sorted = [x[0] for x in arr]

    psB = [0]*(n+1)
    psZ = [0]*(n+1)
    for i in range(1, n+1):
        psB[i] = psB[i-1] + arr[i-1][1]
        psZ[i] = psZ[i-1] + arr[i-1][2]
    totZ = psZ[n]

    ans = 0
    for x in range(1, n+1):
        Ax = aPreSum[x]
        Zx = x - Ax
        tx = x - 2*Ax
        pos = bisect_right(d_sorted, tx) 
        
        part1 = pos * Ax + psB[pos]


        part2 = (n - pos) * Zx + (totZ - psZ[pos])
        ans += part1 + part2

    print(ans)
