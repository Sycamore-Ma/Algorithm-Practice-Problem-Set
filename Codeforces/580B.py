n, d = map(int, input().split())

mapofmoney = {}

for _ in range(n):
    m, s = map(int, input().split())
    if m not in mapofmoney:
        mapofmoney[m] = s
    else:
        mapofmoney[m] += s

# sort the map by keys
sorted_map = sorted(mapofmoney.items())

# # sort the map by values
# sorted_map_by_value = sorted(mapofmoney.items(), key=lambda x: x[1], reverse=True)

# print(type(mapofmoney))
# print(mapofmoney)
# print(type(sorted_map))
# print(sorted_map)

# 针对 value 求 map 的前缀和
# sorted_map = [(k, v) for k, v in sorted_map if v > 0]
sorted_map = [(k, v) for k, v in sorted_map]
# print(type(sorted_map))
for i in range(1, len(sorted_map)):
    sorted_map[i] = (sorted_map[i][0], sorted_map[i][1] + sorted_map[i - 1][1])


# 在首位插入一个
sorted_map.insert(0, (sorted_map[0][0], 0))

# print(sorted_map)

max_socre = 0

l = 1
r = 1

while r < len(sorted_map):
    # if r == 0:
    #     r += 1
    #     max_socre = sorted_map[0][1]
    #     continue
    # if sorted_map[r][0] - sorted_map[l][0] <= d:
    if sorted_map[r][0] - sorted_map[l][0] < d:
        max_socre = max(max_socre, sorted_map[r][1] - sorted_map[l-1][1])
        r += 1
    else:
        l += 1

print(max_socre)