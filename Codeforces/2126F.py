# import sys
# input = sys.stdin.read

# # t = int(input())


# data = input().split()
# idx = 0
# t = int(data[idx])
# idx += 1

# out = []


# for _ in range(t):
#     # n, q = map(int, input().split())
#     # color = list(map(int, input().split()))

#     n, q = int(data[idx]), int(data[idx + 1])
#     idx += 2

#     color = list(map(int, data[idx:idx + n]))
#     idx += n

#     total_cost = 0
#     graph = [[] for _ in range(n)]
#     weight = [{} for _ in range(n)]     # weight[u][color_] = 这些颜色邻边的权重和
    
#     for i in range(n-1):
#         # u, v, w = map(int, input().split())
#         u, v, w = int(data[idx]), int(data[idx + 1]), int(data[idx + 2])
#         idx += 3

#         u -= 1
#         v -= 1
#         graph[u].append((v, w))
#         graph[v].append((u, w))

#         cu, cv = color[u], color[v]

#         weight[u][cv] = weight[u].get(cv, 0) + w
#         weight[v][cu] = weight[v].get(cu, 0) + w

#         if cu != cv:
#             total_cost += w

#     for i in range(q):
#         # x, new_color = map(int, input().split())
#         x, new_color = int(data[idx]), int(data[idx + 1])
#         idx += 2

#         x -= 1

#         old_color = color[x]
#         if old_color == new_color:
#             print(total_cost)
#             continue

#         # for y, w in graph[x]:
#         #     if color[x] != color[y] and new_color == color[y]:
#         #         total_cost -= w
#         #     elif color[x] == color[y] and new_color != color[y]:
#         #         total_cost += w

#         # for c, w in weight[x].items():
#         #     if old_color != c and new_color == c:
#         #         total_cost -= w
#         #     elif new_color != c and old_color == c:
#         #         total_cost += w

#         if weight[x].get(old_color, 0) > 0:
#             total_cost += weight[x][old_color]
#         if weight[x].get(new_color, 0) > 0:
#             total_cost -= weight[x][new_color]

#         for y, w in graph[x]:
#             weight[y][old_color] -= w
#             if weight[y][old_color] == 0:
#                 del weight[y][old_color]
#             weight[y][new_color] = weight[y].get(new_color, 0) + w

#         color[x] = new_color
#         # print(">>>", total_cost)
#         print(total_cost)
# #         out.append(total_cost)
    
# # # print("\n".join(out))
# # sys.stdout.write("\n".join(out) + "\n")

'''
Python 3.7+ 里，字符串会在启动时做一次全局随机种子哈希；但 整数没有——整数哈希就是它本身（再做一次乘常数的混合）。
如果测试数据让很多颜色在混合前高位都一样、低位都落在同一条链上，dict 会退化成长链表；一次查找就可能遍历数十、上百个元素。
RD = getrandbits(16) 随机打乱低 16 位，再异或到所有颜色 & 询问的颜色上，不影响对同/异色的判断，却能把这种「输入卡哈希」的攻击彻底规避。
Python int 的哈希就是它本身（高位还原后做乘法）；若数据出题人故意给出一堆「哈希低 16 位全相同」的颜色，字典会产生碰撞退化（从 O(1) 退到链式查找）。
c ^ RD 随机打散低位，可防极端碰撞——几乎零成本，多测时最稳。
'''

import sys
# iterator = map(int, sys.stdin.buffer.read().split())
data = list(map(int, sys.stdin.buffer.read().split()))
out = []

import random
rd = random.getrandbits(16)

# t = int(input())
# t = next(iterator)
idx = 0
t = data[idx]; idx += 1

for _ in range(t):
    # n, q = map(int, input().split())
    # color = list(map(int, input().split()))

    # n, q = next(iterator), next(iterator)
    # color = [0] * n
    # for i in range(n):
    #     color[i] = next(iterator)

    n, q = data[idx], data[idx+1]; idx += 2
    color = data[idx:idx+n]; idx += n

    color = [c ^ rd for c in color]     # 随机打乱低 16 位，规避输入卡哈希的攻击


    total_cost = 0

    parent = [-1] * n
    weightOfParents = [0] * n  # weightOfParents[u] = weight of edges to color from u's parent
    weightOfSons = [0] * n
    # weightOfSonsWithColor = [{} for _ in range(n)]  # weightOfSonsWithColor[u][color] = weight of edges to color from u's sons

    from collections import defaultdict
    weightOfSonsWithColor = [defaultdict(int) for _ in range(n)]


    for i in range(n-1):
        # u, v, w = map(int, input().split())
        # u, v, w = next(iterator), next(iterator), next(iterator)
        u, v, w = data[idx]-1, data[idx+1]-1, data[idx+2]; idx += 3
        # u -= 1
        # v -= 1

        if parent[v] == -1:
            pass
        else:
            u, v = v, u
            
        parent[v] = u
        weightOfParents[v] = w
        # weightOfSons[u] += w
        # weightOfSonsWithColor[u][color[v]] = weightOfSonsWithColor[u].get(color[v], 0) + w
        weightOfSonsWithColor[u][color[v]] += w

        if color[u] != color[v]:
            total_cost += w

    for i in range(q):
        # v, new_color = map(int, input().split())
        # v, new_color = next(iterator), next(iterator)
        v, new_color = data[idx]-1, data[idx+1]; idx += 2
        # v -= 1

        new_color ^= rd  # 随机打乱低 16 位，规避输入卡哈希的攻击

        old_color = color[v]
        
        if old_color == new_color:
            print(total_cost)
            continue

        color[v] = new_color
        
        pv = parent[v]

        # total_cost += weightOfSonsWithColor[v].get(old_color, 0)
        # # total_cost += weightOfSonsWithColor[v][old_color]
        # total_cost -= weightOfSonsWithColor[v].get(new_color, 0)
        total_cost += weightOfSonsWithColor[v][old_color]
        total_cost -= weightOfSonsWithColor[v][new_color]
        if color[pv] == old_color:
            total_cost += weightOfParents[v]
        if color[pv] == new_color:
            total_cost -= weightOfParents[v]

        # if old_color not in weightOfSonsWithColor[parent[v]]:
        #     weightOfSonsWithColor[parent[v]][old_color] = 0
        # if pv != -1:
        weightOfSonsWithColor[pv][old_color] -= weightOfParents[v]   # v, u 的 weight 也是 u, v 的 weight

        # if new_color not in weightOfSonsWithColor[parent[v]]:
        #     weightOfSonsWithColor[parent[v]][new_color] = 0
        # if pv != -1:
        weightOfSonsWithColor[pv][new_color] += weightOfParents[v]

        # print(">>>", total_cost)
        print(total_cost)

#         out.append(str(total_cost) + '\n')

# sys.stdout.write('\n'.join(out))