n, t = map(int, input().split())

s = input()

for ti in range(t):
    i = 0
    while i < len(s) - 1:
        if s[i] == 'B' and s[i + 1] == 'G':
            s = s[:i] + 'GB' + s[i + 2:]
            i += 2
        else:
            i += 1
        
        # print(">>>", s)

print(s)