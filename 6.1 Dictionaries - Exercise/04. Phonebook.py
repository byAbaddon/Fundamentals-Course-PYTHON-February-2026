di = {}

while True:
    token = input()
    if token.isdigit():
        for x in [input() for _ in range(int(token))]:
            if x not in di:
                print(f'Contact {x} does not exist.')
            else:
                print(x, '->',di[x])
        break

    k, v = token.split('-')
    di[k] = v
