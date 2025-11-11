t = int(input())

# 重排方块，面积不变，更加长条


for _ in range(t):
    a, b = map(int, input().split())
    mul = a * b

    width = 1

    # OK = False
    ANS = -1

    while width * width <= mul:
        if width > 5:
            break
        if width > b:
            break
        if b % width != 0:
            width += 1
            continue
        if mul % width == 0:
            height = mul // width

            if (width + height) % 2 == 0:
                # OK = True
                ANS = (width + height) 
                break
        width += 1

    # print(">>>", ANS)
    print(ANS)