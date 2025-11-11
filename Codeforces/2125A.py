t = int(input())

for i in range(t):
    s = input()
    sorted_s = ''.join(sorted(s, reverse=True))

    print(sorted_s)