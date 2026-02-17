p = list(map(int, input().split(', ')))
m = int(input())

while min(p) < m:
    i = p.index(min(p))
    j = p.index(max(p))
    need = m - p[i]
    give = p[j] - m
    if give <= 0:
        print('No equal distribution possible')
        break
    t = min(need, give)
    p[i] += t
    p[j] -= t
else:
    print(p)
