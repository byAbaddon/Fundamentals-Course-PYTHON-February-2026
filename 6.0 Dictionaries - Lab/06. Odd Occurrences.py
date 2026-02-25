lst = list(map(lambda x: x.lower(), input().split()))
di = {}

for x in lst:
    di[x] = di.get(x,0) + 1

[print(k, end=' ') for k,v in di.items() if v & 1]






