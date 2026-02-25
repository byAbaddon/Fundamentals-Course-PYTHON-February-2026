di = {}

for x in iter(input, 'statistics'):
    k, v = x.split(': ')
    di[k] = di.setdefault(k, 0) + int(v)

print('Products in stock:')
[print(f'- {k}: {v}') for k, v in di.items()]
print(f'Total Products: {len(di)}\nTotal Quantity: {sum(di.values())}')
