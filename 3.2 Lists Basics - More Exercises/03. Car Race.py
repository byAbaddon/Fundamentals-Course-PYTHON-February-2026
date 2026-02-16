lst = [int(x) for x in input().split()]
l = lst[:len(lst) // 2]
r = lst[len(lst) // 2 + 1:][::-1]

l_t = r_t = 0

for n in l:
    if n == 0:
        l_t *= 0.8
        continue
    l_t += n

for n in r:
    if n == 0:
        r_t *= 0.8
        continue
    r_t += n

if l_t < r_t:
    print(f'The winner is left with total time: {l_t:.1f}')
else:
    print(f'The winner is right with total time: {r_t:.1f}')
