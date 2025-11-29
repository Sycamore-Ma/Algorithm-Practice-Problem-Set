import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    visited = [False] * (n+1)
    for i in range(n):
        if p[i] == 0:
            continue
        visited[p[i]] = True

    last = n

    for i in range(n):
        if p[i] == 0:
            for j in range(last, 0, -1):
                if not visited[j]:
                    p[i] = j
                    visited[j] = True
                    last = j - 1
                    break

    # print(">>>", p)

    left = -1
    right = -1

    for i in range(n):
        if p[i] != i+1:
            left = i
            break

    for i in range(n-1, -1, -1):
        if p[i] != i+1:
            right = i
            break

    if left == -1 and right == -1:
        # print(">>>", 0)
        print(0)
        continue
    else:
        # print(">>>", right - left + 1)
        print(right - left + 1)