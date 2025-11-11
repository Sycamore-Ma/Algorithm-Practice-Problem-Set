n = int(input())

cnt = 0

for i in range(n):
    p, q = map(int, input().split())
    if p+1 < q:
        cnt += 1

print(cnt)