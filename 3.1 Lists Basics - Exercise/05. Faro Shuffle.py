lst_deck = input().split()
loop = int(input())

for _ in range(loop):
    mid = len(lst_deck) // 2
    left, right = lst_deck[:mid], lst_deck[mid:]
    lst_deck = [left[i // 2] if i % 2 == 0 else right[i // 2] for i in range(len(lst_deck))]

print(lst_deck)
