loop = int(input())
subtotal = total = 0

while loop:
    loop -= 1

    price = float(input())
    days = int(input())
    caps = int(input())

    if  0.01 <= price <= 100 and  1 <= days <= 31 and 1 <= caps <= 2000:
        subtotal = price * caps * days
        print(f'The price for the coffee is: ${subtotal:.2f}')
        total += subtotal

print(f'Total: ${total:.2f}')

