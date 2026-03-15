s, e = ord(input()), ord(input())
r = 0

for x in input():
    if s < ord(x) < e:
        r += ord(x)

print(r)
