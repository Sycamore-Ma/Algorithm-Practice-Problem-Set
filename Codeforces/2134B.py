t = int(input())    

# a0, a1, a2, a3
# a0 + a0*k -> a0 * (k+1)
# a1 -> a1 * (k+1)


# prime = []

def find_prime(k):
    top = k+1
    if top % 2 == 0:
        return 2
    dev = 3
    while dev * dev <= top:
        if top % dev == 0:
            return dev
        dev += 2
    return top


for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    b = [] * (n + 1)

    p = find_prime(k)
    niyuan_k = pow(k%p, -1, p)

    for ai in a:
        # temp = ai
        # if ai <= k:
        #     temp += ai * k
        # else:       # ai 比 k 大，不能再加 ai 次了
        #     temp += ai * k
        # b.append(temp)

        # temp = ai
        # if ai % 2 == 1:
        #     if k % 2 == 1:
        #         temp += k
        #     else:
        #         temp += 0 
        # else:
        #     temp += 0 

        # b.append(temp)

        temp = (-ai) % p
        add_times = (temp * niyuan_k) % p
        b.append(add_times * k + ai)

    # print(*a)
    # print(">>>", *b, ">>>")
    print(*b)
