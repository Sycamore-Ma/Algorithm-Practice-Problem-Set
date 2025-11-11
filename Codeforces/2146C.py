import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    ans = []
    for i in range(n):
        ans.append(i+1)

    # print(*ans)

    OK = True
    i = 0
    while i < n:
        # 找到连续的 0 开始循环移位
        if s[i] == '0':
            j = i
            while j < n and s[j] == '0':
                j += 1
            
            seg = j - i
            if seg == 1:
                OK = False
                break

            head = ans[i]
            for k in range(i, j-1):
                ans[k] = ans[k+1]
            ans[j-1] = head

            i = j
        else:
            i += 1

    if OK:
        print("YES")
        print(*ans)
        # print(">>>", *ans)
    else:
        print("NO")