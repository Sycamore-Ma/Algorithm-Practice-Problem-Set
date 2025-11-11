import sys
data = sys.stdin.buffer.read().split()
it = iter(map(int, data))

outlines = []

# t = int(input())
t = next(it)

for _ in range(t):
    # n = int(input())
    n = next(it)
    # a = list(map(int, input().split()))
    # b = list(map(int, input().split()))
    a = [next(it) for __ in range(n)]
    b = [next(it) for __ in range(n)]

    ok = True

    if a[-1] != b[-1]:
        ok = False
    else:
        for i in range(n-2, -1, -1):
            # if a[i] != b[i] and a[i] ^ a[i+1] != b[i]:
            # print("---", a[i], b[i+1], (a[i] ^ b[i+1]), b[i])
            # print('>>>', bin(a[i]), bin(b[i+1]), bin(a[i] ^ b[i+1]), bin(b[i]))
            if a[i] != b[i] and ((a[i] ^ b[i+1]) != b[i] and (a[i] ^ a[i+1]) != b[i]):
                ok = False
                break
    
    outlines.append("YES" if ok else "NO")

    # print("YES" if ok else "NO")

print("\n".join(outlines))
