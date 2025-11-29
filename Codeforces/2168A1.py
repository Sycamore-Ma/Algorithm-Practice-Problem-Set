round = input().strip()

if round == "first":
    n = int(input())
    a = list(map(int, input().split()))
    s = []
    for ai in a:
        # s.append(chr(int('a')+ai-1))
        s.append(chr(ord('a')+ai-1))
    print(''.join(s))
else:
    s = input().strip()
    res = []
    for ch in s:
        res.append(str(ord(ch)-ord('a')+1))
    print(len(res))
    print(' '.join(res))