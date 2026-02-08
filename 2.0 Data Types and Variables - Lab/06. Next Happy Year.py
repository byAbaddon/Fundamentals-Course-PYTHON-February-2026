year = int(input())

while True:
    year += 1
    s = str(year)
    if len(s) == len(set(s)):
        print(year)
        break


