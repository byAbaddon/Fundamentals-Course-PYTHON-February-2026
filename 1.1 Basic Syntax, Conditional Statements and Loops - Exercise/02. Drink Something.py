age = int(input())
r = ''

if age <= 14: r = 'toddy'
elif age <= 18: r = 'coke'
elif age <= 21: r = 'beer'
else: r = 'whisky'

print('drink',r)