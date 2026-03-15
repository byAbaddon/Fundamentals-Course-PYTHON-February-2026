from re import finditer

pat = r'-?\d+(\.\d+)?($|(?=\s))'
num = input()
res = finditer(pat, num)
[print(r.group(0), end=' ') for r in res]