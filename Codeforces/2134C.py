import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    sum = 0
    maxsum = 0

    for i in range(n):
        prevsum = sum
        digit = i+1

        cur = 0

        if digit % 2 == 1: # 奇数
            cur = sum - a[i]
        else:
            cur = sum + a[i]

        # if digit % 2 == 1: # 奇数
        #     cur = sum - a[i]
        #     if cur < minsum and i > 0:
        #         ans += minsum - cur
        #         cur = minsum
        #     sum = cur
        # else: # 偶数
        #     sum += a[i]
        
        # minsum = min(minsum, sum)

        # if i > 0 and digit % 2 == 1:
        # if i > 0 and digit % 2 == 1:
        if i > 0:
            if cur < maxsum:
                ans += maxsum - cur
                cur = maxsum
        
        sum = cur
        
        if i > 0:
            maxsum = max(maxsum, prevsum)

    print(ans)
    # print(">>>", ans)