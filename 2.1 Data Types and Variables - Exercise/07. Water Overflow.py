w = 255
current_lt = 0
lst_lt = [int(input()) for _ in range(int(input()))]

while len(lst_lt):
    lt = lst_lt.pop(0)
    current_lt += lt
    if current_lt > w:
        current_lt -= lt
        print('Insufficient capacity!')

print(current_lt)
