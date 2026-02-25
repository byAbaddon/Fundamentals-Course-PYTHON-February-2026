di = {}

for st in input().split():
    for x in st:
        di[x] = di.setdefault(x, 0) + 1

for k, v in di.items():
    print(k, '->', v)
