import sys
input = sys.stdin.readline

t = int(input())

# def pre_check(n, p, s):
#     if s[1] == 1 or s[n] == 1:
#         return False

def set_value(p, s, l, r):
    for i in range(l+1, r):
        if p[i] > min(p[l], p[r]) and p[i] < max(p[l], p[r]):
            s[i] = 1

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    p = p
    x = input().strip()
    x = x
    s = [0] * n
    
    min_pos = -1; min_val = 10**9+7
    max_pos = -1; max_val = -1
    for i in range(n):
        if p[i] < min_val:
            min_val = p[i]
            min_pos = i
        if p[i] > max_val:
            max_val = p[i]
            max_pos = i

    set_value(p, s, min(min_pos, max_pos), max(min_pos, max_pos))
    set_value(p, s, 0, min_pos)
    set_value(p, s, 0, max_pos)
    set_value(p, s, min_pos, n-1)
    set_value(p, s, max_pos, n-1)

    ok = True
    for i in range(n):
        if x[i] == '1' and s[i] == 0:
            ok = False
            break

    if ok:
        print(5)
        print(min(min_pos, max_pos)+1, max(min_pos, max_pos)+1)
        print(0+1, min_pos+1)
        print(0+1, max_pos+1)
        print(min_pos+1, n-1+1)
        print(max_pos+1, n-1+1)
    else:
        print(-1)