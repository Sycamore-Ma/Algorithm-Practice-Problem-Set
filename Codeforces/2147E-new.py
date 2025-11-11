import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    OR_INIT = 0
    for ai in a:
        OR_INIT |= ai

    # print("OR_INIT >>>", OR_INIT)

    addOneCosts = []
    for k in range(32):
        if (OR_INIT >> k) & 1:
            # addOneCosts.append(0)
            continue

        goal = 1 << k
        # fullOneMask = 1 << (k+1) - 1    # 2^(k+1)-1, 构造 111111111...            # DEBUG! 运算优先级错误
        fullOneMask = (1 << (k+1)) - 1    # 2^(k+1)-1, 构造 111111111...

        # print("k, goal, fullOneMask >>>", bin(k), bin(goal), bin(fullOneMask))

        optimal = None
        for ai in a:
            r = ai & fullOneMask
            # curCost = None
            # if r >= goal:
            #     curCost = 0
            # else:
            #     curCost = goal - r
            curCost = goal - r

            if optimal == None or curCost < optimal:
                optimal = curCost
            if optimal == 0:
                break
        if optimal != None:
            addOneCosts.append(optimal)

    addOneCosts.sort()
    # prefSum = []
    # for i in range(len(addOneCosts)+1):
    #     if i == 0:
    #         prefSum.append(0)
    #     else:
    #         prefSum.append(prefSum[-1] + addOneCosts[i-1])

    prefSum = [0]
    for c in addOneCosts:
        prefSum.append(prefSum[-1] + c)

    # print("len(addOneCosts) >>>", len(addOneCosts))

    # print("addOneCosts >>>", addOneCosts)


    for __ in range(q):
        b = int(input())

        low = 0
        high = len(prefSum) - 1

        while low < high:
            mid = (low + high + 1) // 2
            if prefSum[mid] <= b:
                low = mid
            else:
                high = mid - 1

        ans = (OR_INIT.bit_count() + low)
        # print("ans >>>", ans)
        print(ans)


'''
算法还是有问题，所有的低位都靠这个 

例如

1000000
0100000
0010000
0000111

算完或以后变成
1110111

如果只让最后一个数字+1，最后一个数字就变成
0001000 了
所有的 OR 并不是变成了 1111111，而是 1111000
'''