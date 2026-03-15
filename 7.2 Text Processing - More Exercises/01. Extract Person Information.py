for _ in range(int(input())):
    name, age, = '', ''
    for x in input().split():
        if ('@' and '|') in x:
            name = x[x.index('@') + 1: x.rindex('|')]
        if ('#' and '*') in x:
            age = x[x.index('#') + 1: x.rindex('*')]

    print(f'{name} is {age} years old.')
