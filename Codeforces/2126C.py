t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    h = list(map(int, input().split()))

    cur_hight = h[k-1]

    h.sort()
    # h = list(set(h))

    cur_water = 1

    OK = True

    # print(h)

    for hi in h:
        # print(hi, cur_hight, cur_water)
        if cur_water > cur_hight:
            OK = False
            break

        if hi <= cur_hight:
            continue
        if hi > cur_hight:
            cur_water += hi - cur_hight
            if cur_water > cur_hight+1:
                OK = False
                break
            cur_hight = hi

    if OK:
        print("YES")
    else:
        print("NO")



