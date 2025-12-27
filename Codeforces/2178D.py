# 两两打，a 小的那个必死
# 排序后，从小的开始打，每次死一个，肯定能剩下 m 个，但是不满足“歇斯底里”的限制，“歇斯底里”需要打到最后没有人能打（未打过别人）为止，而不是随时停下
# 不可能活超过一半的人数，每次打架至少会死一个人

# 取 m-1 大家伙，打 m-1 小家伙，大家伙都活下来，小家伙全死
# 中间的还没打过 n - m - m + 2
# 中间的 n - 2m + 2 顺次打架，剩下最大的 1 个
# 总共剩下 m-1+1

# 剩下 0 个特殊构造

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    
    # ele[i][0] = a[i], ele[i][1] = i+1
    ele = []

    for i in range(n):
        ele.append([a[i], i+1])

    if m > n // 2:
        print(-1)
        continue

    # a.sort()
    ele.sort()



    # 让一些除了最大 prime、第二大 secon 之外的小罗罗打最大只 prime，打到最大只 prime 的血量刚好比第二大 secon 小，就可以了
    # 换句话说是个背包问题，选一些除了 prime、secon 的小的值加起来，尽可能的大，但不超过 prime_a 本身的值
    # 如果发现，最后这些小罗罗的加和 sigma, prime_a - sigma > secon_a, 那就还不行，因为最后剩的血量还是大于第二大的攻击力

    # 剩下的那些，没有选中的，依次从小攻击大的就可以了，最后一个小罗罗去攻击 secon 就行了
    # 最后一次打架按照 prime 打 secon 来

    def knap_pick_mask(prime_a):
    #     items = ele[:-2]
    #     sum_items = sum(ai for ai, _ in items)
    #     cap = min(prime_a, sum_items)

    #     dp = 1
    #     parent = [-1] * (cap + 1)
    #     parent_item = [-1] * (cap + 1)

    #     full_mask = (1 << (cap + 1)) - 1

    #     for i, (w, _id) in enumerate(items):
    #         if w > cap:
    #             continue

    #         shifted = (dp << w) & full_mask
    #         new = shifted & ~dp

    #         x = new
    #         while x:
    #             lsb = x & -x
    #             s = lsb.bit_length() - 1
    #             parent[s] = s - w
    #             parent_item[s] = i
    #             x ^= lsb

    #         dp |= shifted

    #     sigma = (dp.bit_length() - 1)
    #     if sigma > cap:
    #         sigma = cap

    #     while sigma >= 0 and ((dp >> sigma) & 1) == 0:
    #         sigma -= 1

    #     chosen_ids = set()
    #     mask_items = [False] * len(items)
    #     cur = sigma
    #     while cur > 0:
    #         i = parent_item[cur]
    #         if i < 0:
    #             break
    #         mask_items[i] = True
    #         chosen_ids.add(items[i][1])
    #         cur = parent[cur]

    #     return sigma, chosen_ids, mask_items
        items = ele[:-2]

        sigma = 0
        chosen_ids = set()
        mask_items = [False] * len(items)

        for i, (ai, id) in enumerate(items):
            # if sigma + ai > prime_a:
            if sigma + ai >= prime_a:
                break
            sigma += ai
            chosen_ids.add(id)
            mask_items[i] = True

        return sigma, chosen_ids, mask_items

    if m == 0:
        if n <= 2:
            print(-1)
            continue

        prime_a, prime_id = ele[-1]
        secon_a, secon_id = ele[-2]

        # health_table = {}
        # for ai, id in ele:
        #     health_table[id] = ai

        # alive = set(id for _, id in ele)
        # hasAttacked = set()
        ans = []

        ok = True

        # 哪些小罗罗拿去削 prime
        sigma, used_to_hit_prime, mask_items = knap_pick_mask(prime_a)
        
        if prime_a - sigma > secon_a:
            print(-1)
            continue

        rounds = n - 1
        print(rounds)
        # print(">>> rounds:", rounds)

        for idx in used_to_hit_prime:
            ans.append((idx, prime_id))
            # health_table[prime_id] -= health_table[idx]
            # alive.remove(idx)
            # hasAttacked.add(idx)

        # 剩下的打架
        smallers = []

        for i in range(len(ele)-2):
            if not mask_items[i]:
                smallers.append(ele[i])
        
        for i in range(len(smallers)-1):
            ans.append((smallers[i][1], smallers[i+1][1]))

        # print("------ smallers: ", smallers)
        if len(smallers) > 0:   
            ans.append((smallers[-1][1], secon_id))

        ans.append((prime_id, secon_id))

        for u, v in ans:
            # print(">>>", u, v)
            print(u, v)

        continue






    survivors_big = ele[n-(m-1):n]
    smallers = ele[:m-1]
    middles = ele[m-1: n-(m-1)]
    # print("survivors_big: ", ' '.join(map(str, survivors_big)), end=' ')    
    # print("smallers: ", ' '.join(map(str, smallers)), end=' ')
    # print("middles: ", ' '.join(map(str, middles)), end=' ')

    rounds = m-1 + n-2*(m-1) - 1
    # print("rounds: ", rounds)
    print(rounds)
    for i in range(0, m-1):
        # print(survivors_big[i], smallers[i])
        print(survivors_big[i][1], smallers[i][1])

    for i in range(0, n-2*(m-1)-1):
        # print(middles[i+1], middles[i])
        print(middles[i+1][1], middles[i][1])

