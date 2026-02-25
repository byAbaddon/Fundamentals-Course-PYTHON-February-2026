di_p = {}
di_q = {}

for x in iter(input, 'buy'):
    name, price, quantity = x.split()
    di_p[name] = float(price)
    di_q[name] = di_q.setdefault(name, 0) + int(quantity)

val = list(zip(di_p.values(), di_q.values()))

for i, k in enumerate(di_p):
    print(f'{k} -> {val[i][0] * val[i][1]:.2f}')
