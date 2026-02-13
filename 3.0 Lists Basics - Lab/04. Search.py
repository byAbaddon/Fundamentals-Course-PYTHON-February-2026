lst = [input() for _ in range(int(input()) + 1)]
word = lst.pop(0)

print(lst)
print([x for x in lst if word in x])



