from math import ceil

p, c = int(input()), int(input())

r = p / c
print(c - p if r < 1 else ceil(r))
