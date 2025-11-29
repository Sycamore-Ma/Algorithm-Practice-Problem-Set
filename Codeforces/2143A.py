import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    OK = True
    Assending = True

    for i in range(1, n):
        if p[i] > p[i-1]:
            if Assending:
                continue
            else:
                OK = False
                break

        elif p[i] < p[i-1]:
            Assending = False


    if OK:
        print("YES")
    else:
        print("NO")    