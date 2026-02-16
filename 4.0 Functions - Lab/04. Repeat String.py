def repeat(*args):
    s, n = args
    return s * n

s = input()
n = int(input())
print(repeat(s, n))