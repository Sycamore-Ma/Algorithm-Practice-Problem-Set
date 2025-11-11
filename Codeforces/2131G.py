# m, 1, 2, 1, 2
# m, 1, 2, 1, ???
# m, 1, ???, 1, ???
# 1, m', 1, 2, 1, 2, 1
# 1, m', 1, 2, 1, ???, 1
# 1, m', 1, ???, 1, ???1, 1

mod = 10**9 + 7

def quick_pow(base, a):
    ans = 1
    while a > 0:
        if a & 1:
            ans = (ans * base) % mod
        base = (base * base) % mod
        a >>= 1
    return ans

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = list(map(int, input().split()))

    s.sort()
    ans = 1

    if s[0] != 1:
        times = (k-1) // 2
        ans *= s[0] % mod
        ans *= quick_pow(2, times)
        ans %= mod
    else:
        if k == 1:
            ans = 1
        else:
            times = (k-1-1) // 2
            ans *= s[1] % mod
            ans *= quick_pow(2, times)
            ans %= mod

    print(ans)
    print(">>>", ans)