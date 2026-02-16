def calculation(c, n1, n2):
    r = ''
    match c:
        case 'multiply':
            r = n1 * n2
        case 'divide':
            r = n1 / n2
        case 'add':
            r = n1 + n2
        case 'subtract':
            r = n1 - n2

    return int(r)


command = input()
n1 = int(input())
n2 = int(input())

print(calculation(command, n1, n2))
