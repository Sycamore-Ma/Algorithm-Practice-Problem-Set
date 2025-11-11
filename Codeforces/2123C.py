t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    mins = [0] * n
    maxs = [0] * n

    for i in range(n):
        if i == 0:
            mins[i] = a[i]
            maxs[i] = a[n-1-i]
        else:
            mins[i] = min(mins[i-1], a[i])
            maxs[i] = max(maxs[i-1], a[n-1-i])

    ansstr = ""

    for i in range(n):
        if i == 0 or i == n - 1:
            ansstr += "1"
            continue
        # if mins[i] <= a[i] and maxs[n-1-i] <= a[i]:
        #     ansstr += "1"
        # else:
        #     ansstr += "0"

        if mins[i] < a[i] and maxs[n-1-i] > a[i]:
            ansstr += "0"
        else:
            ansstr += "1"

    # ansstr = '0' * n
    # ansstr = ansstr[:0] + '1' + ansstr[1:]  # First element is always '1'
    # ansstr = ansstr[:n-1] + '1'  # Last element is always '1'

    # for i in range(n):
    #     if i == 0:
    #         continue
    #     if a[i] <= a[i-1]:
    #         # ansstr[i] = '1'
    #         ansstr = ansstr[:i] + '1' + ansstr[i+1:]
    #     else:
    #         break
    
    # for i in range(n-1, -1, -1):
    #     if i == n - 1:
    #         continue
    #     if a[i] >= a[i+1]:
    #         # ansstr[i] = '1'
    #         ansstr = ansstr[:i] + '1' + ansstr[i+1:]
    #     else:
    #         break

    print(ansstr)