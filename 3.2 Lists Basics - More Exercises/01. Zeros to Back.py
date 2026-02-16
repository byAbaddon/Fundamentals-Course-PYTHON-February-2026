lst = [int(x) for x in input().split(', ')]
zero_count = lst.count(0)
print([x for x in lst if x > 0] + [0] * zero_count)
