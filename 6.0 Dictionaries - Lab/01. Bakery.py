lst = input().split()
di = {}

while lst:
    k, v = lst.pop(0),lst.pop(0)
    di[k]=int(v)

print(di)