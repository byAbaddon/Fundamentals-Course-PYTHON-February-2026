for s in [x for x in iter(input, 'End')]:
    if s == 'SoftUni': continue
    collect = ''
    for c in s:
        collect += c * 2
    print(collect)
