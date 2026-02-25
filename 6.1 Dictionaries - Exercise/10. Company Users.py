di = {}

for x in iter(input, 'End'):
    n, _id = x.split(' -> ')
    di.setdefault(n, [])
    if _id not in di[n]:
        di[n].append(_id)


for k, v in di.items():
    print(k)
    [print('--',x) for x in v]
