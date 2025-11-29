t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    cnt = [-1] * (2*n + 10)

    for i in range(2*n):
        if cnt[a[i]] == -1:
            cnt[a[i]] = 0
        cnt[a[i]] += 1

    cnt_even = 0
    cnt_odd = 0

    for i in range(2*n + 10):
        if cnt[i] == -1:
            continue
        if cnt[i] % 2 == 0:
            cnt_even += 1
        else:
            cnt_odd += 1

    ans = 0

    if cnt_odd > 0:
        ans = cnt_odd + cnt_even * 2
    else:
        # n 为 偶数，n 中合法个数为 偶数：xxxxoo，xxxxxo
        # n 为 奇数，n 中合法个数为 奇数：xxxxxoo，xxxxxxo
        if n % 2 == cnt_even % 2:
            ans = cnt_even * 2
        else:
            # 有一个失配
            ans = (cnt_even-1) * 2

    print(ans)
    # print(">>>", ans)
