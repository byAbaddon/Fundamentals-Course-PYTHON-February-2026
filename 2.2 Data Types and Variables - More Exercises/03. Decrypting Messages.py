key = int(input())

for c in [input() for _ in range(int(input()))]:
    print(chr(key + ord(c)), end='')
