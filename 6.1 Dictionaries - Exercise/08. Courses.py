di = {}

for x in iter(input, 'end'):
    course, name = x.split(' : ')
    di.setdefault(course, []).append(name)

for k,v in di.items():
    print(f'{k}: {len(v)}')
    [print(f'-- {x}') for x in v]
