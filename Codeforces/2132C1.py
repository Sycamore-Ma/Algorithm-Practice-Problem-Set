t = int(input())

pow_3 = []
coins = []

def init():
    # pow_3.append(0)
    pow_3.append(1)
    while pow_3[-1] <= 10**9:
        pow_3.append(pow_3[-1] * 3)
    
    pow_3.append(pow_3[-1] * 3)
    pow_3.append(pow_3[-1] * 3)
    pow_3.append(pow_3[-1] * 3)
    pow_3.append(pow_3[-1] * 3)
        
    for x in range(len(pow_3)-2):
        if x == 0:
            coins.append(3)
        else:
            coins.append(pow_3[x+1] + x * pow_3[x-1])

init()

for _ in range(t):
    n = int(input())

    cost = 0
    x = 0

    while n > 0:
        rem = n % 3
        if rem != 0:
            cost += rem * coins[x]
        n //= 3
        x += 1

    print(cost)
    # print(">>>", cost)