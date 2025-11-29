t = int(input())

for _ in range(t):
    n = int(input())
    a = str(input())
    m = int(input())
    b = str(input())
    c = str(input())

    i = 0
    for ci in c:
        char = b[i]
        if ci == 'V':
            a = char + a
        else :
            a = a + char
        i += 1
    
    print(a)  
    # print(">>>", a)  