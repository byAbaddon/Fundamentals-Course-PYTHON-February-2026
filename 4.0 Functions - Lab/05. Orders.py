def orders(i,p):
    dict_products = {'coffee': 1.5, 'water': 1.0, 'coke': 1.4, 'snacks': 2.00, }
    print(f'{dict_products[i] * p:.2f}')


orders(input(), float(input()))