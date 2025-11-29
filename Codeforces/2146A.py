import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split())) 

    counter = {}
    for ai in a:
        if ai not in counter:
            counter[ai] = 0
        counter[ai] += 1

    cnt = []
    for item in counter.items():
        # print(item)
        cnt.append(item[1])

    # print(cnt)
    ans = -1
    for candi in cnt:
        temp = 0
        for c in cnt:
            if candi <= c:
                temp += candi
        if temp > ans:
            ans = temp

    print(ans)
    # print(">>>", ans)