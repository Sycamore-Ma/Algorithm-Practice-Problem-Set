n, q = map(int, input().split())

a = list(map(int, input().split()))

# 初始化一个 0 到 n 的差分数组
diff = [0] * (n + 2)

for _ in range(q):
    l, r = map(int, input().split())
    diff[l] += 1
    diff[r + 1] -= 1

# print(diff)

# 计算前缀和得到最终的数组
for i in range(1, n + 2):
    diff[i] += diff[i - 1]


a = sorted(a)
# print(a)
# print(diff)
diff = sorted(diff[1:-1])
# print(diff)

for i in range(n):
    a[i] *= diff[i]

print(sum(a))
