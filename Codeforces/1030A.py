n = int(input())

sum = 0

score = list(map(int, input().split()))

for i in score:
    sum += i

if sum == 0:
    print("EASY")
else:
    print("HARD")