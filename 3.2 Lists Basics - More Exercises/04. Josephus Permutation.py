lst = [int(x) for x in input().split()]
n = int(input()) - 1

res = []
index = 0

while lst:
    index = (index + n) % len(lst)
    res.append(str(lst.pop(index)))

print('[' + ','.join(res) + ']')