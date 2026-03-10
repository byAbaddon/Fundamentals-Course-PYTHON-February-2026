lst = []

for x in input().split(', '):
    correct = False
    if 2 < len(x) < 17:
        for c in x:
            if c.isalpha() or c.isdigit() or '_' == c or c == '-':
                correct = True
            else:
                correct = False
                break
    if correct:
        lst.append(x.strip())

[print(x) for x in lst]