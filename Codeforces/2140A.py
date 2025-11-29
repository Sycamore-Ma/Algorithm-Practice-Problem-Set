t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    t = s
    # 对 t 进行排序
    t = list(t)
    t.sort()
    t = "".join(t)

    # print(s, t)

    cnt = 0
    for i in range(n):
        if s[i] != t[i]:
            cnt += 1

    ans = (cnt + 1) // 2

    print(ans)
    # print(">>>", ans)