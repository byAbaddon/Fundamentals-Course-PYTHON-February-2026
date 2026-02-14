lst_money = input().split(', ')
beggars = int(input())
lst_beggars = [0] * beggars

for i in range(len(lst_money)):
    lst_beggars[i % beggars] += int(lst_money[i])

print(lst_beggars)