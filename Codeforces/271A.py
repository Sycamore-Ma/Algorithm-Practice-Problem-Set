y = int(input())

def checkUniqeDigit(num):
    digits = set()
    for digit in str(num):
        if digit in digits:
            return False
        digits.add(digit)
    return True

while True:
    y += 1
    if checkUniqeDigit(y):
        print(y)
        break
    