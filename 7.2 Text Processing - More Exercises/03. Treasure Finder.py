key = input().split()

for s in iter(input, 'find'):
    r = ''
    k = key * 30
    for x in s:
        r += chr(ord(x) - int(k.pop(0)))

    m = r[r.index('&') + 1: r.rindex('&')]
    c = r[r.index('<') + 1: r.rindex('>')]
    print(f'Found {m} at {c}')
