t = int(input())

for _ in range(t):
    s = input().strip()
    count_Y = s.count('Y')

    if count_Y > 1:
        print("NO")
    else:
        print("YES")