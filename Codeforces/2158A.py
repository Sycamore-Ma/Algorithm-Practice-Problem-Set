t = int(input())

for _ in range(t):
    n = int(input())
    y, r = map(int, input().split())
    print(min(r + y//2, n))
    # print(">>>", r + y//2)
    # print(">>>", r + y//2)
    # print("---", y//2)