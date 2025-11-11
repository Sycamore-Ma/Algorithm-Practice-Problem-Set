import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    evenCnt = 0
    evenNum = []
    evenIdx = []
    for i, ai in enumerate(a):
        if ai % 2 == 0:
            evenCnt += 1
            evenNum.append(ai)
            evenIdx.append(i)

    ok = False

    if evenCnt >= 2:
        ok = True
        print(evenNum[0], evenNum[1])
    elif evenCnt <= 1:
        if evenCnt == 1:
            for i, ai in enumerate(a):
                if ok:
                    break
                if i < evenIdx[0] and (evenNum[0] % ai) % 2 == 0:
                    print(ai, evenNum[0])
                    ok = True
                    break
        
        if not ok:
            if evenCnt == 1:
                # remove the even number from a
                a.pop(evenIdx[0])

            n = len(a)

            for i in range(n):
                if ok:
                    break
                ai = a[i]
                for j in range(i+1, n):
                    aj = a[j]
                    
                    if 2*ai >= aj:
                        print(ai, aj)
                        ok = True
                        break
                    else:
                        break

            if not ok:
                for i in range(n):
                    if ok:
                        break
                    ai = a[i]
                    for j in range(i+1, n):
                        aj = a[j]
                        if (aj % ai) % 2 == 0:
                            print(ai, aj)
                            ok = True
                            break
    
    if not ok:
        print(-1)