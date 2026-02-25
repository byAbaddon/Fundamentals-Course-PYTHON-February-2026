di = {}

for line in iter(input, 'Lumpawaroo'):

    if ' | ' in line:
        side, user = line.split(' | ')

        # if user exist pass
        if any(user in users for users in di.values()):
            continue

        di.setdefault(side, []).append(user)

    else:
        user, side = line.split(' -> ')

        # remove old user form side if in
        for s in di:
            if user in di[s]:
                di[s].remove(user)

        di.setdefault(side, []).append(user)
        print(f'{user} joins the {side} side!')


for side, users in di.items():
    if users:
        print(f'Side: {side}, Members: {len(users)}')
        for u in users:
            print(f'! {u}')
