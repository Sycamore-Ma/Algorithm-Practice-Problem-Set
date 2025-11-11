t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    casinos = []

    for i in range(n):
        l, r, real = map(int, input().split())
        casinos.append((l, r, real))

    # casinos.sort(key=lambda x: (x[1], x[0], x[2]))
    casinos.sort(key=lambda x: (x[2], x[1], x[0]))

    for i in range(n):
        l, r, real = casinos[i]
        if k >= l and k <= r and k <= real:
            k = real

    # print(">>>", k)
    print(k)