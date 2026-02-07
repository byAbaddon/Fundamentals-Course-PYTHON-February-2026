lst = input().split(', ')

if lst[::-1].pop(0) == 'wolf':
    print('Please go away and stop eating my sheep')
else:
    x = lst.index('wolf')
    print(f'Oi! Sheep number {len(lst[x + 1:])}! You are about to be eaten by a wolf!')
