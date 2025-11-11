n = int(input())

maxcap = 0
cur = 0

for i in range(n):
    a, b = map(int, input().split())
    cur = cur - a + b
    maxcap = max(maxcap, cur)

print(maxcap)