di_con_pas = {k: v for x in iter(input, 'end of contests') for k, v in [x.split(':')]}
di = {}

for x in iter(input, 'end of submissions'):
    con, pas, name, pts = x.split('=>')

    if con in di_con_pas and di_con_pas[con] == pas:  # validate con and pass
        if name not in di or con not in di[name]:
            di.setdefault(name, {})[con] = int(pts)
        else:  # check points <
            if di[name][con] < int(pts):
                di[name][con] = int(pts)

can_name = ''
max_pts = 0
for k, v in di.items():
    if max_pts < sum(v.values()):
        max_pts = sum(v.values())
        can_name = k

print(f'Best candidate is {can_name} with total {max_pts} points.\nRanking:')
sorted_di = dict(sorted(di.items()))

for key, val in sorted_di.items():
    print(key)
    for k, v in sorted(val.items(), key=lambda x: -x[1]):
        print(f'#  {k} -> {v}')
