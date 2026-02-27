di = {}

for token in iter(input, 'Season end'):
    if 'vs' not in token:
        name, area, skl = token.split(' -> ')
        skl = int(skl)

        if name not in di:
            di[name] = {area: skl}

        if area not in di[name]:
            di[name].update({area: skl})

        if skl > di[name][area]:
            di[name][area] = skl
    else:
        name_one, name_two = token.split(' vs ')
        if name_one in di and name_two in di:
            common = set(di[name_one]) & set(di[name_two])
            if common:
                sum_one = sum(di[name_one].values())
                sum_two = sum(di[name_two].values())
                if sum_one > sum_two:
                    del di[name_two]
                elif sum_two > sum_one:
                    del di[name_one]

di_by_skl = {}

for key, val in di.items():
    for k, v in val.items():
        di_by_skl[key] = di_by_skl.setdefault(key, 0) + v

for n, s in sorted(dict(di_by_skl).items(), key=lambda x: (-x[1], x[0])):
    print(f'{n}: {s} skill')
    for k, v in sorted(di[n].items(), key=lambda x: (-x[1], x[0])):
        print(f'- {k} <::> {v}')
