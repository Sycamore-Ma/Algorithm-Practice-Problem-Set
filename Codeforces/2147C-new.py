import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    # s = "#" + s + "#"
    s = "1" + s + "1"

    OKOK = True

    # if "11011" in s:
        # OKOK = False
        # print("NO")
    # elif "#1011" in s:
    #     print("NO")
    # elif "1101#" in s:
    #     print("NO")
    # elif "#101#" in s:
    #     print("NO")
    # else:
    #     print("YES")

    s_new_1 = []
    s_new_0 = []

    s_new_1.append(s[0])
    for i in range(1, n+2):
        if s[i-1] == "1" and s[i] == "1":
            s_new_1.append("#")
        else:
            s_new_1.append(s[i])

    s_new_1 = "".join(s_new_1)
    # 将所有的 "1#" 替换为 "##"
    s_new_1 = s_new_1.replace("1#", "##")

    s_new_0.append(s_new_1[0])
    for i in range(1, n+2):
        if s_new_1[i-1] == "0" and s_new_1[i] == "0":
            s_new_0.append("*")
        else:
            s_new_0.append(s_new_1[i])
    s_new_0 = "".join(s_new_0)
    s_new_0 = s_new_0.replace("0*", "**")


    # print(">>>", s, s_new_1, s_new_0)

    i = 0
    while i < n+2:
        if s_new_0[i] == "#":
            # 找到下一个 #，中间必须全是非 *
            j = i+1
            visited_star = False
            while j < n+2 and s_new_0[j] != "#" and not visited_star:
                if s_new_0[j] == "*":
                    visited_star = True
                j += 1
            
            if j >= n+2:
                break

            if visited_star:
                i = j
                continue
            
            length = j - i - 1
            if length == 0:
                i = j
                continue
            if (length//2) % 2 == 0:
                OKOK = False
                break
            i = j
        else:
            i += 1
                    

    if OKOK:
        # print("\n ----------- YES")
        print("YES")
    else:
        # print("\n ----------- NO")
        print("NO")


    # 1010101 还是不行，这是奇数个，中间 0 会被漏掉