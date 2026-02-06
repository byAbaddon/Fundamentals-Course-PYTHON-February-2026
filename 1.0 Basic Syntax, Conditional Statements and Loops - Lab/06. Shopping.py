budget = int(input())

while True:
    try:
        budget -= int(input())
        if budget < 0:
            print('You went in overdraft!')
            break
    except:
        break

if budget >= 0:
    print('You bought everything needed.')
