di = {}

for _ in range(int(input())):
    color, name, damage, health, armor = input().split()
    damage = int(damage) if damage != 'null' else 45
    health = int(health) if health != 'null' else 250
    armor = int(armor) if armor != 'null' else 10

    di.setdefault(color, {})[name] = {'damage': damage, 'health': health, 'armor': armor}

for color, dragons in di.items():
    d_avg = sum(d['damage'] for d in dragons.values()) / len(dragons)
    h_avg = sum(d['health'] for d in dragons.values()) / len(dragons)
    a_avg = sum(d['armor'] for d in dragons.values()) / len(dragons)

    print(f'{color}::({d_avg:.2f}/{h_avg:.2f}/{a_avg:.2f})')
    for name, stats in sorted(dragons.items()):
        print(f'-{name} -> damage: {stats["damage"]}, health: {stats["health"]}, armor: {stats["armor"]}')
