word , re_word = input(), input()
collection = ''

for i in range(len(word)):
    if word[i] != re_word[i]:
        collection = re_word[0:i + 1] + word[i + 1:100]
        print(collection)

