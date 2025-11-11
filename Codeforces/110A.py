number = input()

OK = True
cnt_lucky = 0

for char in number:
    if char in '47':
        cnt_lucky += 1

lucky_number = str(cnt_lucky)

for char in lucky_number:
    if char not in '47':
        OK = False
        break

if OK:
    print('YES')
else:
    print('NO')