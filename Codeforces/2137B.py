t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    # s0, s1, s2 = [], [], []

    # for i in range(1, n+1):
    #     if i % 3 == 0:
    #         s0.append(i)
    #     elif i % 3 == 1:
    #         s1.append(i)
    #     else:
    #         s2.append(i)

    ans = []

    for x in p:
        # if x % 3 == 0:
        #     ans.append(s0.pop())
        # elif x % 3 == 1:
        #     ans.append(s2.pop())
        # else:
        #     ans.append(s1.pop())
        ans.append(n-x+1)


    # print(">>>")
    print(" ".join(map(str, ans)))

