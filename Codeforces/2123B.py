t = int(input())

for _ in range(t):
    n, j, k = map(int, input().split())
    a = list(map(int, input().split()))
    flag = a[j-1]

    # sort the a in descending order
    a.sort(reverse=True)

    # if a[k-1] <= flag:
    #     print("YES")
    # else:
    #     print("NO")

    if k >= 2:
        print("YES")
    else:
        if flag < a[0]:
            print("NO")
        else:
            print("YES")