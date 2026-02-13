lst = [int(input()) for _ in range(int(input()))]
com = input()

match com:
    case 'even':
        r = [x for x in lst if not x % 2]
    case 'odd':
        r = [x for x in lst if x % 2]
    case 'negative':
        r = [x for x in lst if x < 0]
    case 'positive':
        r = [x for x in lst if x >= 0]

print(r)
