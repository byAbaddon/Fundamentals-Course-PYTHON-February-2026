string = ''
result = 0

for _ in range(int(input())):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    calc = (snowball_weight  / snowball_time)  ** snowball_quality
    if calc >= result:
        result = calc
        string = f'{snowball_weight} : {snowball_time} = {int(calc)} ({snowball_quality})'

print(string)