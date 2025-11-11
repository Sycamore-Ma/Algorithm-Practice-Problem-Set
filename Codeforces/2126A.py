t = int(input())

def findLowestDigit(num):
    return min(int(digit) for digit in str(num))

for _ in range(t):
    n = int(input())
    print(findLowestDigit(n))
