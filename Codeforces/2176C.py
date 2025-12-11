t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # 最大的 ODD, EVEN, EVEN, EVEN
    # EVEN 前缀和

    odd_cnt = 0
    even_cnt = 0
    optimal_odd_val = -1
    evens = []

    for i in range(n):
        if a[i] % 2 == 0:
            even_cnt += 1
            evens.append(a[i])
        else:
            odd_cnt += 1
            optimal_odd_val = max(optimal_odd_val, a[i])

    evens.sort(reverse=True)
    even_prefix_sum = [0] * (even_cnt + 10)

    for i in range(even_cnt):
        even_prefix_sum[i+1] = even_prefix_sum[i] + evens[i]

        
    anses = []

    for k in range(1, n+1):
        if odd_cnt == 0:
            anses.append(0)
        else:
            # 注释：满足最大加和，就要尽可能一个最大奇数，然后尽可能把所有偶数用上
            # k-1-even_cnt 是最少需要的额外奇数（平凡奇数）个数
            # 这个数字需要是偶数才能把最大的那个奇数留住，记为 low_even 个平凡奇数
            # 至少需要拿多少偶数个平凡奇数：low_even

            low_even = max(0, k-1-even_cnt)
            if low_even & 1:
                low_even += 1
            
            if low_even > odd_cnt-1:
                anses.append(0)
                continue

            left_even_cnt = min(even_cnt, k-1, k-1-low_even)

            if left_even_cnt < 0:
                anses.append(0)
            else:
                ans = optimal_odd_val + even_prefix_sum[left_even_cnt]
                anses.append(ans)

    print(' '.join(map(str, anses)))
    # print('> '.join(map(str, anses)))


