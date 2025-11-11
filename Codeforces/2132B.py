t = int(input())

for _ in range(t):
    n = int(input())
    ans = []
    base = 10
    while base <= n-1:
        count = base+1
        if n % count == 0:
            ans.append(n // count)
        base *= 10
    
    print(len(ans))
    if len(ans) == 0:
        # ans.append(0)
        # print(0)
        continue
    else :
        ans.sort()
        print(*ans)
        # print(">>>", *ans)