lst = input().split()

while True:
    token = input().split()

    if token[0] == 'No':
        lst = [x for x in lst if x is not None]
        print(*lst)
        break

    if token[0] == 'OutOfStock':
        lst = [x if x != token[1] else None for x in lst]

    if token[0] == 'Required':
        gift, index = token[1], int(token[2])
        if 0 <= index < len(lst):
            lst[index] = gift

    if token[0] == 'JustInCase':
        lst.pop()
        lst.append(token[1])
