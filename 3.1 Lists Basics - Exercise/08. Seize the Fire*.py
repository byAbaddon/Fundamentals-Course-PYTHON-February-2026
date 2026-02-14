lst_data = input().split('#')
water = int(input())

effort = fire = 0

print('Cells:')
for data in lst_data:
    fire_type, value = data.split(' = ')
    cell = int(value)

    if fire_type == 'High' and not (81 <= cell <= 125):
        continue
    if fire_type == 'Medium' and not (51 <= cell <= 80):
        continue
    if fire_type == 'Low' and not (1 <= cell <= 50):
        continue

    if water >= cell:
        water -= cell
        fire += cell
        effort += cell * 0.25
        print(f' - {cell}')

print(f'Effort: {effort:.2f}\nTotal Fire: {fire}')

