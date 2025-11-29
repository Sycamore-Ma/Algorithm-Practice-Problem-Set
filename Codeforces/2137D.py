import sys
input = sys.stdin.readline


# from collections import defaultdict

t = int(input())
out = []

for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))

    # table = {}
    # for i in range(n):
    #     bi = b[i]
    #     table.setdefault(bi, []).append(i)


    # table = defaultdict(list)     # TLE 的根本，没必要使用字典，改用静态数组就可以了
    table = [[] for _ in range(n+1)]
    for i in range(n):
        bi = b[i]
        table[bi].append(i)

    OK = True
    tot_times = 0
    # for bi, idx_list in table.items():
    for bi in range(1, n+1):
        idx_list = table[bi]
        # tot_times += len(idx_list) // bi
        if len(idx_list) % bi != 0:
            OK = False
            break

    # if not OK or tot_times != n:
    if not OK:
        # print(-1)
        out.append("-1")
        continue

    a = [0] * n
    a_used = 1
    # for bi, idx_list in table.items():
    for bi in range(1, n+1):
        idx_list = table[bi]
        for i in range(0, len(idx_list), bi):
            # print("---", bi, idx_list[i:i+bi])
            # block = idx_list[i:i+bi]
            # for idx in block:

            # for idx in idx_list[i:i+bi]:
            for j in range(i, i+bi):
                idx = idx_list[j]
                a[idx] = a_used
            a_used += 1

    # print(">>>", *a)
    # print(*a)
    out.append(" ".join(map(str, a)))

print("\n".join(out))