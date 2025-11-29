t = int(input())

a = []

def check(v):
    temp = [1 if ai >= v else -1 for ai in a]
    temp_prefix = [0] * (n+1)

    for i in range(1, n+1):
        temp_prefix[i] = temp_prefix[i-1] + temp[i-1]


for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

