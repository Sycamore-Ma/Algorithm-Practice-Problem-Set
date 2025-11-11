t = int(input())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    s = list(map(int, input().split()))

    lcm_list = []
    for i in range(n):
        lcm_list.append(lcm(p[i], s[i]))

    p_ = [0] * n
    s_ = [0] * n

    for i in range(n):
        if i == 0:
            p_[i] = lcm_list[i]
        else:
            p_[i] = gcd(p_[i-1], lcm_list[i])

    for i in range(n-1, -1, -1):
        if i == n-1:
            s_[i] = lcm_list[i]
        else:
            s_[i] = gcd(s_[i+1], lcm_list[i])

    # print("p:", p)
    # print("s:", s)
    # print("lcm:", lcm_list)
    # print("p_:", p_)
    # print("s_:", s_)

    if s == s_ and p == p_:
        print("YES")
    else:
        print("NO")
