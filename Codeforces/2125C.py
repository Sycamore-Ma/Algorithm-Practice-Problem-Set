# t = int(input())

prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
single_prime = prime[:4]

candidates = []
sign = 1

for in_ex in range(1, 5):
    if in_ex == 1:
        sign = 1
    elif in_ex == 2:
        sign = -1
    elif in_ex == 3:
        sign = 1
    elif in_ex == 4:
        sign = -1

    from itertools import combinations
    for comb in combinations(single_prime, in_ex):
        product = 1
        for p in comb:
            product *= p
            # print(p, end = ' ')
        candidates.append(product * sign)
        # print(product * sign)

# print(candidates)


def countGoodNumbers(r):
    cnt = 0

    for c in candidates:
        # cnt += r // c
        # print(c, "->", r // c)

        sign_here = 1 if c > 0 else -1
        cnt += sign_here * (r // abs(c))
        # print(c, "->", r // abs(c), "sign:", sign_here)

        # 100 / -35 -> 3
        # 100 / 35 -> 2

    cnt = r - cnt
    return cnt - 1      # 1 不是素数！！！

    

t = int(input())

for _ in range(t):
    l, r = map(int, input().split())

    ans = countGoodNumbers(r) - countGoodNumbers(l - 1)
    print(ans)