from re import findall

collect = ''

while True:
    data = input()
    if data == '':  break

    collect += data + ' '

res = findall(r'[0-9]{1,}', collect)
print(' '.join(res))

