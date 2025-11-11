t = int(input())
for _ in range(t):
    n = int(input())
    l = []
    r = []
    s = []
    ans = 0
    sum_left = 0

    for i in range(n):
        li, ri = map(int, input().split())
        l.append(li)
        r.append(ri)
        s.append(li+ri)
        ans += ri - li
        sum_left += li

    l.sort(), r.sort()
    if n//2 > 0:
        pick_left = sum(l[:n//2])
        pick_right = sum(r[-(n//2):])
        ans += pick_right - pick_left
    
    add = 0
    s.sort(reverse=True)
    add += sum(s[:n//2])
    add -= sum_left

    if n % 2 == 1:
        l.sort(reverse=True)
        add += l[n//2]

    ans += add

    # # 选两个对，最大权匹配，2e5 非枚举
    # # 需要保证不能来自同一区间

    # l = []
    # r = []
    # ans = 0
    # for i in range(n):
    #     li, ri = map(int, input().split())
    #     l.append((li, i))
    #     r.append((ri, i))
    #     ans += ri-li

    # l.sort()
    # r.sort()

    # sum_r = 0
    # visited = [False] * n


    # for k in range(n//2):
    #     ri, i = r[n-1-k]
    #     visited[i] = True
    #     sum_r += ri

    # sum_l = 0
    # cnt = 0
    # for k in range(n):
    #     if cnt >= n//2:
    #         break
    #     if not visited[k]:
    #         sum_l += l[k][0]
    #         cnt += 1

    # add = sum_r - sum_l

    # ans += add






    # # l2 = r
    # # r2 = l
    # # l = l2
    # # r = r2


    # l.sort()
    # r.sort()

    # sum_r = 0
    # visited = [False] * n


    # for k in range(n//2):
    #     ri, i = r[n-1-k]
    #     visited[i] = True
    #     sum_r += ri

    # sum_l = 0
    # cnt = 0
    # for k in range(n):
    #     if cnt >= n//2:
    #         break
    #     if not visited[k]:
    #         sum_l += l[k][0]
    #         cnt += 1

    # add = sum_r - sum_l

    # ans += add









    print(ans)
    # print(">>>", ans)

# 2
# 2
# 1 4
# 2 3
# 2
# 1 3
# 2 4

# 6
# 7
