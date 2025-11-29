import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    # s = "#" + s + "#"

    # if "11011" in s:
    #     print("NO")
    # elif "#1011" in s:
    #     print("NO")
    # elif "1101#" in s:
    #     print("NO")
    # elif "#101#" in s:
    #     print("NO")
    
    # else:
    #     print("YES")

    # OKOK = True
    # for i in range(1, n-1):
    #     if s[i-1] == "1" and s[i] == "0" and s[i+1] == "1":
    #         ok = False
    #         if i-2 >= 0 and s[i-2] == "0":
    #             ok = True
    #         if i+2 < n and s[i+2] == "0":
    #             ok = True
    #         if not ok:
    #             OKOK = False
    #             break

    # # 寻找 10101010101 ... 的重复
    # i = 0
    # while i < n:
    #     if s[i] == "0":
    #         i += 1
    #         continue
    #     j = i+1
    #     while j < n and s[j] != s[i]:
    #         j += 1
        
    #     if s[i] == "1" and s[j-1] == "1" and i-1 >= 0 and s[i-1] == "1":
    #         length = j - i
    #         zero_cnt = length // 2
    #         if length % 2 == 1:
    #             OKOK = False
    #             break
    #     i = j


    s = "1" + s + "1"

    if "11011" in s:
        print("NO")
    elif "#1011" in s:
        print("NO")
    elif "1101#" in s:
        print("NO")
    elif "#101#" in s:
        print("NO")
    
    else:
        print("YES")


    if OKOK:
        print("\n ----------- YES")
        # print("YES")
    else:
        print("\n ----------- NO")
        # print("NO")


    # 1010101 还是不行，这是奇数个，中间 0 会被漏掉