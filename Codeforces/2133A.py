t = int(input())

for _ in range(t):
    n = int(input())

    a = list(map(int, input().split()))

    OK = False

    for i in range(n):
        for j in range(i+1, n):
            if a[i] == a[j]:
                OK = True
                break

    if OK:
        print("YES")
    else:
        print("NO")