lst = [5, 7, 11]

for i in range(1, int(input()) + 1):
    if i < 10:
        print(i, '->', i in lst)
    else:
        a, b = str(i)
        r = (int(a) + int(b)) in lst
        print(i, '->', r)
