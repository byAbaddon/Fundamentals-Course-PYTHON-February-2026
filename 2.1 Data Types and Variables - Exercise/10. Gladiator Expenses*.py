lost_fights, helmet_price, sword_price, shield_price, armor_price = [float(input()) for _ in range(5)]
fights = shield_breaks = money = 0

while True:
    if int(lost_fights) == fights:
        print(f'Gladiator expenses: {money:.2f} aureus')
        break

    fights += 1
    damage_helmet = damage_sword = False


    if fights % 2 == 0:
        money += helmet_price
        damage_helmet = True

    if fights % 3 == 0:
        money += sword_price
        damage_sword = True

    if damage_helmet and damage_sword:
        money += shield_price
        shield_breaks += 1

        if shield_breaks % 2 == 0:
            money += armor_price
