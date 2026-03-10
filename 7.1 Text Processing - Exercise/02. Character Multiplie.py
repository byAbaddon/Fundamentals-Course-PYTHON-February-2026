a, b = input().split()
s = sum(ord(a[i]) * ord(b[i]) for i in range(min(len(a), len(b))))
s += sum(ord(c) for c in a[min(len(a), len(b)):])
s += sum(ord(c) for c in b[min(len(a), len(b)):])
print(s)


