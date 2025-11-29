n = int(input())
s = input()

cntA, cntD = 0, 0

for char in s:
    if char == 'A':
        cntA += 1
    elif char == 'D':
        cntD += 1

if cntA > cntD:
    print('Anton')
elif cntD > cntA:
    print('Danik')
else:
    print('Friendship')