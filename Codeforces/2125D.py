import sys
iterator = map(int, sys.stdin.buffer.read().split())


mod = 998244353

# n, m = map(int, input().split())
n, m = next(iterator), next(iterator)

# ls = []
# rs = []
# ps = []
# qs = []

segements = []

dp_ans = [0] * (m+1)
dp_ans[0] = 1

MEMORY = 10000000

invmods = [-1] * MEMORY
basepos = [-1] * MEMORY

def fast_pow(base, po):
    if base >= MEMORY:
        ans = 1
        while po > 0:
            if po % 2:
                ans = ans * base % mod
            base = base * base % mod
            po >>= 1
        return ans
    else:
        ans = 1
        basebase = base
        while po > 0:
            if po % 2:
                ans = ans * base % mod
            base = base * base % mod
            po >>= 1
        basepos[basebase] = ans
        return ans

def invmod(x):
    # return pow(x, mod-2, mod)

    if x >= MEMORY:
        return fast_pow(x, mod - 2)
    else:
        if invmods[x] == -1:
            invmods[x] = fast_pow(x, mod - 2)
        return invmods[x]


# Y, N, Y, N, N, Y
# pq, 1-pq, pq, 1-pq, 1-pq, pq
# Y/N*N, N, Y/N*N, N, N, Y/N*N
# pq/(1-pq)*(1-pq), (1-pq), pq/(1-pq)*(1-pq), (1-pq), (1-pq), pq/(1-pq)*(1-pq)

ALL_DONT_SELECT = 1


for _ in range(n):
    # l, r, p, q = map(int, input().split())
    l, r, p, q = next(iterator), next(iterator), next(iterator), next(iterator)
    # ls.append(l)
    # rs.append(r)
    # ps.append(p)
    # qs.append(q)

    select_prop = p * invmod(q) % mod
    dont_select_prop = (1-select_prop+mod) % mod

    s_d = select_prop * invmod(dont_select_prop) % mod

    # segements.append((l, r, p, q))
    # segements.append((l, r, select_prop, dont_select_prop))
    segements.append((l, r, s_d))
    
    # ALL_DONT_SELECT = ALL_DONT_SELECT * (1 - p * invmod(q) % mod + mod) % mod
    ALL_DONT_SELECT = ALL_DONT_SELECT * dont_select_prop % mod


segements.sort(key=lambda x: (x[1], x[0]))


for s in segements:
    # l, r, p, q = s
    # l, r, select_prop, dont_select_prop = s

    l, r, s_d = s

    # print("seg: ", l, r, p, q)

    # dp_ans[r] = dp_ans[r] + dp_ans[l-1] * p / q

    # select_prop = p * invmod(q) % mod
    # dont_select_prop = (1-select_prop+mod) % mod

    # dp_ans[r] = dp_ans[r] + dp_ans[l-1] * select_prop * (1-select_prop+mod) % mod
    # dp_ans[r] = (dp_ans[r] + dp_ans[l-1] * select_prop * dont_select_prop) % mod
    # dp_ans[r] = (dp_ans[r] + dp_ans[l-1] * select_prop * invmod(dont_select_prop)) % mod

    dp_ans[r] = (dp_ans[r] + dp_ans[l-1] * s_d) % mod

    # dp_ans[r] %= mod

    

# print("dp_ans: ", dp_ans[m] * ALL_DONT_SELECT % mod)
print(dp_ans[m] * ALL_DONT_SELECT % mod)


