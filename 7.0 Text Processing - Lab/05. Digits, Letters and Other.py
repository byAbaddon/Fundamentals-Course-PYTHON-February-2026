di = {'digit': '' , 'alpha' : '', 'symbol' : ''}
for x in input():
    if x.isdigit(): di['digit'] += x
    elif x.isalpha(): di['alpha'] += x
    else: di['symbol'] += x

print("\n".join(di.values()))