lst = list(iter(input, 'stop'))
di = {}

while lst:
    k, v = lst.pop(0), int(lst.pop(0))
    di[k] = di.setdefault(k, 0) + int(v)

for k, v in di.items():
    print(k, '->', v)
