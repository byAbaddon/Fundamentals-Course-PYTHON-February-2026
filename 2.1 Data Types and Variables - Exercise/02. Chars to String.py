def concat(a, b, c):
    print(a + b + c)


concat(*[input() for _ in range(3)])
