n = float(input())

if n == 0:
    print('zero')
elif abs(n) < 1:
    print('small positive' if n > 0 else 'small negative')
elif abs(n) < 1_000_000:
    print('positive' if n > 0 else 'negative')
else:
    print('large positive' if n > 0 else 'large negative')

