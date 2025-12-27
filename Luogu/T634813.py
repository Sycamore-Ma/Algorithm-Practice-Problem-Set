n, x, y = map(int, input().split())

# cnt = 0

for _ in range(n):
    a, b = map(int, input().split())
    if x >= y:
        continue
    if a <= x:
        x -= a
        # cnt += 1
        x += b

# print(cnt)
print(x)