loop = int(input())
while loop:
    loop -= 1
    n = int(input())
    if n % 2:
        print(n, 'is odd!')
        exit()

print('All numbers are even.')
