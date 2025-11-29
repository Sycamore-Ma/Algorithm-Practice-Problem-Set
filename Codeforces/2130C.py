# No loop is the best solution

par = []
def init_union_tree(n):
    global par
    par = list(range(n))

def find(x):
    if par[x] != x:
        par[x] = find(par[x])
    return par[x]

def unite(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        par[root_y] = root_x

def check(x, y):
    return find(x) == find(y)





t = int(input())

for _ in range(t):
    n = int(input())

    init_union_tree(2*(n+100))

    a = []
    b = []

    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)

    ans = []
    for i in range(n):
        if check(a[i], b[i]):
            continue
        else:
            unite(a[i], b[i])
            ans.append(i+1)

    print(len(ans))
    print(*ans)
