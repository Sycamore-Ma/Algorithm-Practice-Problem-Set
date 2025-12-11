t = int(input())

def check_all_ones(s):
    for char in s:
        if char != '1':
            return False
    return True

def right_shift_by_one(s):
    return s[-1] + s[:-1]

for _ in range(t):
    n = int(input())
    s = input().strip()

    # print("origin s:", s)

    # ans = 0
    # while not check_all_ones(s):
    #     t = right_shift_by_one(s)

    #     # s = t | s
    #     s = ''.join('1' if s[i] == '1' or t[i] == '1' else '0' for i in range(n))
        
    #     print(">>>", s)

    aixs = -1

    for i in range(n):
        if s[i] == '1':
            aixs = i
            break

    ans = 0
    last_one_idx = aixs
    i = aixs + 1

    while True:
        j = i % n
        
        if s[j] == '1':
            # print(">>> last_one_idx:", last_one_idx)
            # print(">>> i, j:", i, j)
            gap = (j+n - last_one_idx - 1) % n
            # print("gap:", gap)
            ans = max(ans, gap)
            last_one_idx = j
            # print("======")

        i += 1
        if j == aixs:
            break

    print(ans)
    # print(">>>>>>", ans)
