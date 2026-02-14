lst = [int(x) for x in input().split()]
n = int(input())
lst_current = sorted(lst)[n:]


result = [str(x) for x in lst if x in lst_current]
print(', '.join(result))

