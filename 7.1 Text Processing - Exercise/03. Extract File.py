for s in input().split('\\'):
    if '.' in s:
        a, b = s.split('.')
        print(f'File name: {a}\nFile extension: {b}')
