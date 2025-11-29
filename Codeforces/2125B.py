t = int(input())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

for _ in range(t):
    a, b, k = map(int, input().split())

    ans = 1
    times = gcd(a, b)

    length_a = a // times
    length_b = b // times

    if length_a <= k and length_b <= k:
        ans = 1
    else:
        ans = 2

    print(ans)
    # print(">>>", ans)
    