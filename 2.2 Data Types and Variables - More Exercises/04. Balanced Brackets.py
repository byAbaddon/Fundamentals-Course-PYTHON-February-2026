bracket = 0
for ch in [input() for _ in range(int(input()))]:
    if ch == '(': bracket += 1
    elif ch == ')': bracket -= 1
    if bracket not in (0, 1): print("UNBALANCED"); exit()

print('BALANCED')