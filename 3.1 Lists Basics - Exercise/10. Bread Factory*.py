input_list = input().split('|')
energy, coins = 100, 100

while input_list:
    event, num = input_list.pop(0).split('-')
    num = int(num)

    if event == 'rest':
        gained = min(num, 100 - energy)
        energy += gained
        print(f'You gained {gained} energy.')
        print(f'Current energy: {energy}.')

    elif event == 'order':
        if energy >= 30:
            energy -= 30
            coins += num
            print(f'You earned {num} coins.')
        else:
            energy += 50
            print('You had to rest!')

    else:
        if coins >= num:
            coins -= num
            print(f'You bought {event}.')
        else:
            print(f'Closed! Cannot afford {event}.')
            exit()

print(f'Day completed!\nCoins: {coins}\nEnergy: {energy}')
