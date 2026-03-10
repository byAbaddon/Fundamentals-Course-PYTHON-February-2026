# A 65
# a 97
total = 0

for x in input().split():
    first, num, last = x[0], int(x[1:-1]), x[-1]

    first_pos = ord(first.upper()) - ord('A') + 1
    last_pos = ord(last.upper()) - ord('A') + 1

    if first.isupper(): r = num / first_pos
    else: r = num * first_pos

    if last.isupper(): r -= last_pos
    else:  r += last_pos

    total += r

print(f'{total:.2f}')

