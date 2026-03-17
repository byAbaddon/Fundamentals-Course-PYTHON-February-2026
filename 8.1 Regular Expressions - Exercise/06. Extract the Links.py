from re import finditer

lines = []
while True:
    line = input()
    if line == '': break

    lines.append(line)

pat = r'www\.[A-Za-z0-9-]+(\.[a-z]+)+'
for line in lines:
    for lnk in finditer(pat, line):
        print(lnk[0])
