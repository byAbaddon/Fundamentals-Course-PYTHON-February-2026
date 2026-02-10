from math import floor

group, all_days = int(input()), int(input())
days = 0
coins = 0

while days != all_days:

    days += 1

    # every ten day
    if not days % 10:
        group -= 2

    # every fifteenth day
    if not days % 15:
        group += 5


    # every day
    coins += 50
    # food_spend
    coins -= group * 2

    # party
    if not days % 3:
        coins -= group * 3

    # kill boss
    if not days % 5:
        coins += group * 20
        # party and bods
        if not days % 3:
            coins -= group * 2



print(f'{group} companions received {floor(coins / group)} coins each.')
