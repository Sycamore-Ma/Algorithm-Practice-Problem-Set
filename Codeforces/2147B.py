import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = []
    for i in range(n-1, 0, -1):
        a.append(i)
    a.append(n)

    for i in range(n):
        a.append(i+1)
    
    print(*a)