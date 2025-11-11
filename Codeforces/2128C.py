# 4 6 7
# 4 0 0, 4 2 0, 4 6 0, 4 6 3, 4 6 7

# 4 6 8
# 4 0 0, 4 2 0, 4 6 0, 4 6 3, 4 6 7?

t = int(input())

for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    ok = True

    min_b_prefix = b[0]
    for i in range(1, n):
        if b[i] >= min_b_prefix * 2:
            ok = False
            break
        else:
            min_b_prefix = min(min_b_prefix, b[i])
    
    if ok:
        print("YES")
    else:
        print("NO")