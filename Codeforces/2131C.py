import sys
# input = sys.stdin.readline

data = sys.stdin.buffer.read().split()

it = iter(map(int, data))

# tt = int(input())
# tt = int(data[0])
tt = next(it)

# from collections import Counter
from collections import defaultdict


import random
rd = random.getrandbits(16)
# 随机打乱低 16 位，规避输入卡哈希的攻击


out_lines = []

for _ in range(tt):
    # n, k = map(int, input().split())
    # n, k = int(data[2*_+1]), int(data[2*_+2])
    n, k = next(it), next(it)

    # S = list(map(int, input().split()))
    # T = list(map(int, input().split()))
    # S = list(map(int, data[2*_+3:2*_+3+n]))
    # T = list(map(int, data[2*_+3+n:2*_+3+2*n]))
    # S = [next(it) for __ in range(n)]
    # T = [next(it) for __ in range(n)]


    # S_dict = {}
    # T_dict = {}

    # for s in S:
    #     if s % k not in S_dict:
    #         S_dict[s % k] = 0
    #     S_dict[s % k] += 1

    # for t in T:
    #     if t % k not in T_dict:
    #         T_dict[t % k] = 0
    #     T_dict[t % k] += 1
    
    # S_dict = Counter(s % k for s in S)
    # T_dict = Counter(t % k for t in T)

    S_dict = defaultdict(int)
    T_dict = defaultdict(int)

    for __ in range(n):
        s = next(it)
        r = s % k
        rr = k - r
        # S_dict[min(r, rr)] += 1
        S_dict[min(r, rr) ^ rd] += 1

    for __ in range(n):
        t = next(it)
        r = t % k
        rr = k - r
        # T_dict[min(r, rr)] += 1
        T_dict[min(r, rr) ^ rd] += 1

    ans = True

    # checked = set()

    # for key in set(S_dict.keys()) | set(T_dict.keys()):

    #     if key in checked:
    #         continue

    #     circleS = S_dict.get(key, 0) + S_dict.get(k - key, 0)
    #     circleT = T_dict.get(key, 0) + T_dict.get(k - key, 0)

    #     if circleS != circleT:
    #         ans = False
    #         break

    #     checked.add(key)
    #     checked.add(k - key)

    # if S_dict != T_dict:
    #     ans = False

    # if ans:
    #     print("YES")
    # else:
    #     print("NO")

    out_lines.append("YES" if S_dict == T_dict else "NO")

print('\n'.join(out_lines))