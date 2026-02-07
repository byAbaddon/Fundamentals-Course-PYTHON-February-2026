for s in [input() for _ in range(int(input()))]:
    if any(c in s for c in ',._'):
        print(s, 'is not pure!')
    else:
        print(s, 'is pure.')