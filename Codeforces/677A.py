# n, h = int(input()), int(input())

n, h = map(int, input().split())

# a = []
# for i in range(n):
#     a.append(int(input()))

a = list(map(int, input().split()))

width = 0

for ai in a:
    if ai > h:
        width += 2
    else:
        width += 1

print(width)