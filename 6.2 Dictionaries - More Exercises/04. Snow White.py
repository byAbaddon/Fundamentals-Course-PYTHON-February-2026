di = {}

for token in iter(input, 'Once upon a time'):
    name, color, pts = token.split(' <:> ')
    pts = int(pts)

    if color not in di:
        di[color] = {}
    if name not in di[color] or pts > di[color][name]:
        di[color][name] = pts

sort_list = [
    [name, pts, len(dwarfs), color]
    for color, dwarfs in di.items()
    for name, pts in dwarfs.items()
]

sort_list.sort(key=lambda x: (-x[1], -x[2]))

for name, pts, count, color in sort_list:
    print(f"({color}) {name} <-> {pts}")



#------------------------------------TODO-----------------------------


di = {}

for token in iter(input, 'Once upon a time'):
    name, color, pts = token.split(' <:> ')
    pts = int(pts)

    if color not in di:
        di[color] = {name: pts}
    if name not in di[color]:
        di[color].update({name: pts})

    if pts > di[color][name]:
        di[color][name] = pts

sort = sorted(di.items(), key=lambda x: (-max(x[1].values()), -len(x[1])))
for c, val in sort:
    for n, p in val.items():
        print(f'({c}) {n} <-> {p}')
