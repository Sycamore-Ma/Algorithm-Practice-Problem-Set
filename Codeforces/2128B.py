t = int(input())

def is_ascending(p3, p2, p1):
    return p3 < p2 < p1

def is_descending(p3, p2, p1):
    return p3 > p2 > p1

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    l = 0
    r = n-1

    q = []
    ans = ""

    operation = 'X'

    in_four = False

    while l <= r:
        left_candidate = p[l]
        right_candidate = p[r]
    
        if len(q) < 3:
            operation = 'L'
        else:
            q3, q2, q1 = q[-3], q[-2], q[-1]

            if in_four:
                in_four = False
            # 如果创造出来了四连跪，上一个三连跪已经留下了一个一定会解开的情况
                if is_ascending(q3, q2, q1):
                    if left_candidate < q1:
                        operation = 'L'
                    elif right_candidate < q1:
                        operation = 'R'

                elif is_descending(q3, q2, q1):
                    if left_candidate > q1:
                        operation = 'L'
                    elif right_candidate > q1:
                        operation = 'R'
            # 如果没有创造四连跪，随便追加一个上去，总之已经解除警报了
                else:
                    operation = 'L'

            else:
            # 判断三连跪，如果有，创造四连跪
                if is_ascending(q3, q2, q1):
                    in_four = True
                    if left_candidate < right_candidate:
                        operation = 'R'
                    else:
                        operation = 'L'
                elif is_descending(q3, q2, q1):
                    in_four = True
                    if left_candidate < right_candidate:
                        operation = 'L'
                    else:
                        operation = 'R'
            # 如果没有三连跪，随便追加一个上去
                else:
                    operation = 'L'

        if operation == 'L':
            if len(q) < 3:
                q.append(left_candidate)
            else:
                q[-3] = q[-2]
                q[-2] = q[-1]
                q[-1] = left_candidate
            l += 1
        else:
            if len(q) < 3:
                q.append(right_candidate)
            else:
                q[-3] = q[-2]
                q[-2] = q[-1]
                q[-1] = right_candidate
            r -= 1

        # ans += operation
        print(operation, end='')

    # print(ans)
    print()


            
