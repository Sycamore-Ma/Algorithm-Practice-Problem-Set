t = int(input())

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

for _ in range(t):
    n = int(input())

    point_pairs = []

    for i in range(n):
        a, b = map(int, input().split())
        point_pairs.append((a, b, i+1))

    point_pairs.sort(key=lambda x: x[0])

    pairs_left = point_pairs[:n//2]
    pairs_right = point_pairs[n//2:]

    pairs_left.sort(key=lambda x: x[1])
    pairs_right.sort(key=lambda x: x[1])

    for i in range(n//2):
        print(pairs_left[i][2], pairs_right[n//2-1-i][2])
