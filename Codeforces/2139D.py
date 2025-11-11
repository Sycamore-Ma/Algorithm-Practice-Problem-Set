import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    
    
#     a = [0] + a

#     reversePair2 = [False] * (n+1)
#     for i in range(1, n-1):
#         if a[i] > a[i+2]:
#             reversePair2[i] = True

#     reverseTri = [False] * (n+1)
#     for i in range(1, n-1):
#         if a[i] > a[i+1] and a[i+1] > a[i+2]:
#             reverseTri[i] = True


#     # pref_odd = [0] * (n+1)
#     # pref_even = [0] * (n+1)
#     # for i in range(1, n+1):
#     #     pref_odd[i] = pref_odd[i-1]
#     #     pref_even[i] = pref_even[i-1]
#     #     if reversePair2[i]:
#     #         if i % 2 == 0:
#     #             pref_odd[i] += 1
#     #         else:
#     #             pref_even[i] += 1
#     pref = [0] * (n+1)
#     for i in range(1, n+1):
#         pref[i] = pref[i-1]
#         # if reversePair2[i]:
#         if reverseTri[i]:
#             pref[i] += 1

#     for qi in range(q):
#         l, r = map(int, input().split())
#         if l == r or l + 1 == r:    # 一个或者两个元素
#             print("YES")
#             continue

#         RightSmaller = r - 2
#         # cnt_odd = pref_odd[RightSmaller] - pref_odd[l-1]
#         # cnt_even = pref_even[RightSmaller] - pref_even[l-1]

#         # if cnt_odd == 0 and cnt_even == 0:

#         cnt = pref[RightSmaller] - pref[l-1]

#         if cnt == 0:
#             print("YES")
#         else:
#             print("NO")



# # 反例：
# # 3 1 2
# # YES


# 不是紧挨着的三元组逆序也会出问题，因为总会遇到相邻的情况

    # 单调栈计算最近的前一个更大元素
    LeftBigger = [-1] * n
    st = []
    for i in range(n):
        while st and a[st[-1]] <= a[i]:
            st.pop()
        if st:
            LeftBigger[i] = st[-1]
        st.append(i)

    # 单调栈计算最近的后一个更小元素
    RightSmaller = [n] * n
    st = []
    for i in range(n - 1, -1, -1):
        while st and a[st[-1]] >= a[i]:
            st.pop()
        if st:
            RightSmaller[i] = st[-1]
        st.append(i)

    INF = n + 5
    cnt = [INF] * n         # x 位置的数作为最大值时，右侧最早小数的位置
    for j in range(n):
        if LeftBigger[j] != -1 and RightSmaller[j] != n:
            x, y = LeftBigger[j], RightSmaller[j]
            if y < cnt[x]:
                cnt[x] = y

    suf = [INF] * (n + 1)   # 后缀
    for i in range(n - 1, -1, -1):
        suf[i] = min(cnt[i], suf[i+1])

    print(">>> suf:", suf)

    for _ in range(q):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        if r >= suf[l]:
            print("NO")
        else:
            print("YES")