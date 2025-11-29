t = int(input())

from bisect import bisect_right

for _ in range(t):
    n, m, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort(reverse=True)
    b.sort(reverse=True)


    whole_cards = []
    player = []
    posA, valA = [], []
    posB, valB = [], []

    i = 0
    j = 0
    while i < n or j < m:
        takeA = False
        if j >= m:
            takeA = True
        elif i >= n:
            takeA = False
        else:
            if a[i] >= b[j]:
                takeA = True
            else:
                takeA = False

        if takeA:
            whole_cards.append(a[i])
            player.append(0)
            posA.append(len(whole_cards))
            valA.append(a[i])
            i += 1
        else:
            whole_cards.append(b[j])
            player.append(1)
            posB.append(len(whole_cards))
            valB.append(b[j])
            j += 1

    # 前缀和
    pre_sum_whole_cards = [0] * (len(whole_cards) + 1)
    for i, c in enumerate(whole_cards):
        tmp = c + pre_sum_whole_cards[i]
        pre_sum_whole_cards[i + 1] = tmp

    # prefA：前 i 个里 a 的数量
    prefA = [0]
    cnt = 0
    for s in player:
        if s == 0: cnt += 1
        prefA.append(cnt)

    # a/b 在各自出现顺序上的值前缀和（便于区间和）
    SA = [0]
    for v in valA: SA.append(SA[-1] + v)

    SB = [0]
    for v in valB: SB.append(SB[-1] + v)

    out = []
    for _ in range(q):
        x, y, z = map(int, input().split())
        # 直接处理 z=0 的快速返回
        if z == 0:
            out.append("0")
            continue

        # 不加限制时取前 z 个
        KA = prefA[z]
        KB = z - KA

        if KA <= x and KB <= y:
            out.append(str(whole_cards[z]))
            continue

        if KA > x:
            # 需要减少 d 个 A，增加 d 个 b
            d = KA - x

            # 前 z 中 a 的个数 idxA（就是 KA）
            idxA = KA  # = bisect_right(posA, z)
            # 删掉 a 的最后 d 个（在 valA 的 idxA-d+1..idxA ）
            dropA = SA[idxA] - SA[idxA - d]

            # z 之后 b 的开头 d 个
            # 先找 z 以内 b 的个数
            idxB = bisect_right(posB, z)
            addB = SB[idxB + d] - SB[idxB]

            out.append(str(whole_cards[z] - dropA + addB))
        else:
            # KB > y，对称操作：减少 d 个 B，增加 d 个 a
            d = KB - y

            idxB = KB  # = bisect_right(posB, z)
            dropB = SB[idxB] - SB[idxB - d]

            idxA = bisect_right(posA, z)
            addA = SA[idxA + d] - SA[idxA]

            out.append(str(whole_cards[z] - dropB + addA))

    print("\n".join(out))
