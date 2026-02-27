ban_words = input().split(', ')
txt = input()

for ban in ban_words:
    txt = txt.replace(ban, '*' * len(ban))

print(txt)