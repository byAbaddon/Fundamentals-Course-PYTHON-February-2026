res, buf, n = '', '', ''

for c in input():
    if c.isdigit():
        n += c
    else:
        if n:
            res += buf * int(n)
            buf , n = '', ''
        buf += c

res += buf * int(n)

res = res.upper()
print(f'Unique symbols used: {len(set(res))}\n{res}')
