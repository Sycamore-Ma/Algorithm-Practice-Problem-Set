n, k1, k2 = map(int, input().split())

max_a = -1

for _ in range(n):
    a, x, y = map(int, input().split())
    if x == 1 and y == 1:
        continue
    if x == 1:
        a -= k1
    if y == 1:
        a -= k2
    if a > 0:
        max_a = max(max_a, a)

print(max_a)