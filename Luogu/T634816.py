n, k = map(int, input().split())

p = list(map(int, input().split()))

q = int(input())

import bisect
def getInterval(x):
    idx = bisect.bisect_right(p, x)
    idx -= 1
    return p[idx], idx

for _ in range(q):
    i, j = map(int, input().split())

    if i > j:
        i, j = j, i

    left, left_idx = getInterval(i)
    right, right_idx = getInterval(j)

    ans = 0
    if i == j:
        ans = 1
    elif left_idx == right_idx:
        ans = 2
    elif left_idx <= right_idx:
        ans = 2
        
        if i != left:
            left_idx += 1
        if j == p[right_idx + 1] - 1:
            right_idx += 1

        ans += max(right_idx - left_idx, 0)

    # print(">>>", left, right, left_idx, right_idx)
    # print(">>>", ans)
    print(ans)


