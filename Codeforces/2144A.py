import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    OK = False
    for l in range(1, n-1):
        if OK:
            break
        for r in range(l+1, n):
            sum1 = sum(a[0:l])
            sum2 = sum(a[l:r])
            sum3 = sum(a[r:n])

            # print("l, r", l, r, sum1, sum2, sum3)
            # print("a", a[0:l], a[l:r], a[r:n])

            s1 = sum1 % 3
            s2 = sum2 % 3
            s3 = sum3 % 3

            if not OK and (s1 == s2 == s3 or s1 != s2 and s2 != s3 and s1 != s3):
                OK = True
                # print(l+1, r+1)
                print(l, r)
                # print(">>>", l+1, r+1)
                break

    if not OK:
        print(0, 0)