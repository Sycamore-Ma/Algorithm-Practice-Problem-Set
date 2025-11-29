t = int(input())

for _ in range(t):
    n = int(input())
    s = list(input().strip())
    t = list(input().strip())

    ans = 0
    opers = []

    def flip(l, r):
        for i in range(l, r+1):
            if s[i] == '0':
                s[i] = '1'
            else:
                s[i] = '0'
        global ans
        ans += 1
        global opers
        opers.append((l+1, r+1))
    
    for i in range(n):
        if i >= n-2:
            break
        if s[i] == t[i]:
            continue
        else:
            # xx
            if i+1 < n and s[i] == s[i+1]:
                flip(i, i+1)
            # xox
            elif i+2 < n and s[i] != s[i+1] and s[i] == s[i+2]:
                flip(i, i+2)
            # xoo
            elif i+2 < n and s[i] != s[i+1] and s[i] != s[i+2]:
                flip(i+1, i+2)
                flip(i, i+2) 

    # print("--- s: ", str(s))
    # print("--- t: ", str(t))
    # print(">>> ans:", ans)
    # print(">>> opers:", opers)

    # 最后剩下 2 位
    # 反着来往前数，但是得归位
    # 前面两个如果一样，就翻转前两个，再三个一起转

    
    # for i in range(n-2, n):
    #     if s[i] == t[i]:
    #         continue
    #     else:
    #         # x

    print(ans)
    for op in opers:
        print(op[0], op[1])