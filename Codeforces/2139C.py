t = int(input())
for _ in range(t):
    k, x = map(int, input().split())

    ans = []

    a = x
    b = 2 ** (k+1) - x

    # 倒着走
    while a != b:
        if a < b:
            ans.append('1')
            b -= a
            a *= 2
        else:
            ans.append('2')
            a -= b
            b *= 2
    
    print(len(ans))
    print(" ".join(reversed(ans)) if ans else "")