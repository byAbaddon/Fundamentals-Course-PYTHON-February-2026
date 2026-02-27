di = {}

for token in iter(input, 'no more time'):
    name, con, pts = token.split(' -> ')
    pts = int(pts)

    if con not in di:
        di[con] = {}

    if name not in di[con] or di[con][name] < pts:
        di[con][name] = pts

for con, users in di.items():
    print(f'{con}: {len(users)} participants')
    for i, (name, pts) in enumerate(
            sorted(users.items(), key=lambda x: (-x[1], x[0])), 1):
        print(f'{i}. {name} <::> {pts}')

print('Individual standings:')

total = {}
for users in di.values():
    for name, pts in users.items():
        total[name] = total.get(name, 0) + pts

for i, (name, pts) in enumerate(
        sorted(total.items(), key=lambda x: (-x[1], x[0])), 1):
    print(f'{i}. {name} -> {pts}')
