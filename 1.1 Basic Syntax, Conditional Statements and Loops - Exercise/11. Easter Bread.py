budget = float (input())
price_bred = float(input())

price_egs = price_bred * 0.75
price_milk = price_bred * 1.25 / 4

one_bred = price_bred + price_egs + price_milk
count_bred = count_egs = 0


while True:
    if budget < one_bred:
        break
    budget -= one_bred
    count_egs += 3
    count_bred += 1
    if not count_bred % 3:
        count_egs -= count_bred - 2



print(f'You made {count_bred} loaves of Easter bread! Now you have {count_egs} eggs and {budget:.2f}BGN left.')
