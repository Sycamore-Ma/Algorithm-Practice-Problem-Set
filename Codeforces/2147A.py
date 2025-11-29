import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())

    if y > x:
        print("2")
        # print(">>>", "2")
    elif y == x:
        print("-1")
        # print(">>>", "-1")
    elif y < x:
        seg1 = 1
        seg2 = y
        seg3 = x - seg1
        if seg2 <= seg1 or seg3 <= seg2:
            print("-1")
            # print(">>>", "-1")
        else:
            print("3")
            # print(">>>", "3")
            # print(">>>", seg1, seg2, seg3)