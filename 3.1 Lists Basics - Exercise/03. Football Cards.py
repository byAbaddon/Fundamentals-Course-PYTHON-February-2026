a = b = 11
seen = set()

for c in input().split():
    if c in seen:
        continue
    seen.add(c)
    a -= c[0] == 'A'
    b -= c[0] == 'B'
    if a < 7 or b < 7:
        break

print(f'Team A - {a}; Team B - {b}')
if a < 7 or b < 7:
    print('Game was terminated')
