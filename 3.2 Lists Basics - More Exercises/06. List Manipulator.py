lst = list(map(int, input().split()))

while True:
    token = input()
    if token == 'end':
        break

    parts = token.split()

    odds = [x for x in lst if x % 2 != 0]
    evens = [x for x in lst if x % 2 == 0]

    if parts[0] == 'exchange':
        i = int(parts[1])
        if i < 0 or i >= len(lst):
            print('Invalid index')
        else:
            lst = lst[i+1:] + lst[:i+1]

    elif parts[0] in ('max', 'min'):
        cmd, kind = parts
        source = odds if kind == 'odd' else evens

        if not source:
            print('No matches')
        else:
            value = max(source) if cmd == 'max' else min(source)
            for i in range(len(lst)-1, -1, -1):
                if lst[i] == value:
                    print(i)
                    break

    elif parts[0] in ('first', 'last'):
        count = int(parts[1])
        kind = parts[2]

        if count > len(lst):
            print('Invalid count')
            continue

        source = odds if kind == 'odd' else evens

        if parts[0] == 'first':
            print(source[:count])
        else:
            print(source[-count:])

print(lst)
