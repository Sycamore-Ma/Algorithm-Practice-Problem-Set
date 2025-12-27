t = int(input())

for _ in range(t):
    s = input().strip()
    opers = 0
    if s[0] == 'u':
        s = 's' + s[1:]
        opers += 1
    if s[-1] == 'u':
        s = s[:-1] + 's'
        opers += 1

    i = 0
    while i < len(s):
        if s[i] == 'u':
            j = i
            while j < len(s) and s[j] == 'u':
                j += 1
            length = j - i
            opers += length // 2
            i = j
        else:
            i += 1

    print(opers)
    # print(">>>", opers)