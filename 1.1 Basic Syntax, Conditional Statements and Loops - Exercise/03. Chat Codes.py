for n in [int(input()) for _ in range(int(input()))]:
    match n:
        case _ if n == 86:
            print('How are you?')
        case _ if (not 86 == n or not n == 88) and n < 88:
            print('GREAT!')
        case _ if n == 88:
            print('Hello')
        case _ if n > 88:
            print('Bye.')
