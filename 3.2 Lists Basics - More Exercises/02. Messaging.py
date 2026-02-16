lst = input().split()
s = list(input())

nums = [sum([int(c) for c in x]) for x in lst]
res = ''

for n in nums:
    n %= len(s)
    res += s.pop(n)

print(res)
