import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a1 = list(map(int, input().split()))
    a2 = list(map(int, input().split()))

    # down in the middle m
    # 0, 1, 2, 3, ..., m-1, m
    # m, m+1, m+2, ..., n-1

    a1_min_from_left = [10**6] * n
    a1_max_from_left = [0] * n
    a2_min_from_right = [10**6] * n
    a2_max_from_right = [0] * n

    temp_min = 10**6
    temp_max = 0
    
    for i, a1i in enumerate(a1):
        temp_min = min(temp_min, a1i)
        temp_max = max(temp_max, a1i)
        a1_min_from_left[i] = temp_min
        a1_max_from_left[i] = temp_max

    temp_min = 10**6
    temp_max = 0

    for i in range(n-1, -1, -1):
        a2i = a2[i]
        temp_min = min(temp_min, a2i)
        temp_max = max(temp_max, a2i)
        a2_min_from_right[i] = temp_min
        a2_max_from_right[i] = temp_max


    max_left = [0] * (2*n+10)

    for m in range(n):
        m_min = min(a1_min_from_left[m], a2_min_from_right[m])
        m_max = max(a1_max_from_left[m], a2_max_from_right[m])
        max_left[m_max] = max(max_left[m_max], m_min)

    ans = 0
    temp = 0
    for upper in range(1, 2*n+1):
        if max_left[upper] > temp:
            temp = max_left[upper]      # max_left[upper] == 3, left could be 1 2 3
        ans += temp

    print(ans)
    # print(">>>", ans)
