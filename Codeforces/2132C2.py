# # # coins[x+1] - 3*coins[x] = 3^x
# # # deals += 2


# pow_3 = []
# coins = []

# def init():
#     # pow_3.append(0)
#     pow_3.append(1)
#     while pow_3[-1] <= 10**9:
#         pow_3.append(pow_3[-1] * 3)
    
#     pow_3.append(pow_3[-1] * 3)
#     pow_3.append(pow_3[-1] * 3)
#     pow_3.append(pow_3[-1] * 3)
#     pow_3.append(pow_3[-1] * 3)
        
#     for x in range(len(pow_3)-2):
#         if x == 0:
#             coins.append(3)
#         else:
#             coins.append(pow_3[x+1] + x * pow_3[x-1])


t = int(input())

def get_minimal_deals(n):
    deals = 0
    while n > 0:
        rem = n % 3
        if rem != 0:
            deals += rem
        n //= 3
    return deals

for _ in range(t):
    n, k = map(int, input().split())
    minimal_deals = get_minimal_deals(n)

    if minimal_deals > k:
        print(-1)
    else:
        k = min(k, n)

        combine_times = (n - k + 1) // 2  
        final_coins = 3 * n     # cheapest

        # at cost 1, 3, 9, 27, 81, ...
        pow_3 = 1  # 3^0
        while combine_times > 0 and pow_3 <= n:
            take = n // (3 * pow_3)
            take = min(combine_times, take)
            final_coins += take * pow_3
            combine_times -= take
            pow_3 *= 3

        print(final_coins)