t = input()
p = 0
r = []

for i, c in enumerate(t):
    if c == '>':
        p += int(t[i+1])
        r.append(c)
    elif p:
        p -= 1
    else:
        r.append(c)

print(''.join(r))
