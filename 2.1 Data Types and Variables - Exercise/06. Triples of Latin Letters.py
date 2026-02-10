e = 97 + int(input())

for a in range(97, e):
    for b in range(97, e):
        for c in range(97, e):
            print(chr(a), chr(b), chr(c), sep='')
