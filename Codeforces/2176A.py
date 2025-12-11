t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    flag = [0] * (n+1)

    for i in range(n):
        for j in range(i+1, n):
            if j >= n:
                break
            if a[i] > a[j]:
                flag[j] = 1
                
    print(sum(flag))
    # print(">>>", flag)
    # print(">>>", sum(flag))