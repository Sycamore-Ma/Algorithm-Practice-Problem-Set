t = int(input())

for _ in range(t):
    n = int(input())

    # cnt_n1 = (n+1) // 2

    for i in range(n):
        if i % 2 == 0:
            print(-1, end=' ')
        else:
            # print(cnt_n1+1, end=' ')
            if i == n - 1:
                print(2, end=' ')
            else:
                print(3, end=' ')
    print()