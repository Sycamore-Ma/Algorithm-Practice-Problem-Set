import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    n = r-l+1

    sum = 0
    ans = [-1] * (n+1)

    used = [False] * (n+1)

    # k = 0
    # base = 1
    # while base < r:
    #     base *= 2
    #     k += 1

    k = r.bit_length()
    # print("k >>>", k)

    for ki in range(k, 0, -1):
        mask = (1 << ki) - 1
        # print("ki, mask >>>", ki, bin(mask))

        for a in range(l, r+1):
            idx_a = a - l
            if used[idx_a]:
                continue
            
            b = (a ^ mask)
            if b < l or b > r:
                continue
            
            idx_b = b - l
            if used[idx_b]:
                continue

            used[idx_a] = True
            used[idx_b] = True
            sum += (a | b) * 2

            ans[idx_a] = b
            ans[idx_b] = a

    for a in range(l, r+1):
        idx_a = a - l
        if used[idx_a]:
            continue
        
        used[idx_a] = True
        sum += a
        ans[idx_a] = a

    print(sum)
    print(*ans[:-1])
    # print(">>>", sum)
    # print("ans >>>", *ans[:-1])