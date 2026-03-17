from re import findall

text = input()
regex = r'((?<=\s)[a-z0-9]+([\.\-_]?[a-z0-9]+)*@[a-z0-9]+([\.\-_]?[a-z0-9]+)*\.[a-z0-9]+([\.\-_]?[a-z0-9]+)*)'
for result in findall(regex, text):
    print(result[0])