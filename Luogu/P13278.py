import sys
input = sys.stdin.readline  # 开启读入挂，提高读入速度

n, m, q = map(int, input().split())
attack = list(map(int, input().split()))

# # health_me = m
# # health_enemy = m

# # attack_me = []
# # attack_enemy = []

# presum_me = [0] * (n + 1)
# presum_enemy = [0] * (n + 1)
# presum_enemy_attack_count = [0] * (n + 1)

# health_me = m
# me_death_time = n + 1

# for i in range(n):
#     a = attack[i]
#     if a >= 0:
#         # health_enemy -= a
#         # attack_enemy.append(a)
#         # attack_me.append(0)
#         presum_enemy[i + 1] = presum_enemy[i] + a
#         presum_enemy_attack_count[i + 1] = presum_enemy_attack_count[i] + 1
#         presum_me[i + 1] = presum_me[i]
#     else:
#         # health_me -= a
#         # attack_me.append(-a)
#         # attack_enemy.append(0)
#         presum_enemy[i + 1] = presum_enemy[i]
#         presum_enemy_attack_count[i + 1] = presum_enemy_attack_count[i]
#         presum_me[i + 1] = presum_me[i] + (-a)

#         health_me -= (-a)
#         if health_me <= 0:
#             me_death_time = i + 1

# # import bisect
# # me_death_time = bisect.bisect_left(presum_me, m)

# for _ in range(q):
#     x = int(input())

#     health_enemy = presum_enemy[me_death_time-1] + x * presum_enemy_attack_count[me_death_time-1]
    

#     # # upper_bound 或者 lower_bound 寻找第一个大于等于 health_me 的位置
#     # time_enemy = bisect.bisect_left(presum_enemy, health_enemy)

#     # print(presum_me, me_death_time)
#     # print(presum_enemy, health_enemy, presum_enemy_attack_count)
    
#     # if time_me < time_enemy:


#     if health_enemy < m:
#         if me_death_time >= n + 1:
#             print("Tie")
#         else:
#             print("No")
#     else:
#         print("Yes")


health_me = m
attack_count = 0
attack_to_enemy = 0
me_death_time = -1

for i in range(n):
    if attack[i] < 0:
        health_me -= -attack[i]
        if health_me <= 0 and me_death_time == -1:
            me_death_time = i
            break
    else:
        attack_count += 1
        attack_to_enemy += attack[i]

for _ in range(q):
    x = int(input())
    health_enemy = attack_to_enemy + x * attack_count
    # if health_enemy < m:
    #     if me_death_time == -1:
    #         print("Tie")
    #     else:
    #         print("No")
    # else:
    #     print("Yes")

    if health_enemy >= m:
        print("Yes")
    elif me_death_time == -1:
        print("Tie")
    else:
        print("No")