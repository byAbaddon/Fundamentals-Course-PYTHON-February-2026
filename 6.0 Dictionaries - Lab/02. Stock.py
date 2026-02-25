lst = input().split()
itm = input().split()

di = {lst[x]: int(lst[x + 1]) for x in range(0, len(lst), 2)}

for x in itm:
    if di.get(x):
        print(f'We have {di[x]} of {x} left')
    else:
        print('Sorry, we don\'t have', x)