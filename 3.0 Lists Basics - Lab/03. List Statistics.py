lst = [int(input()) for _ in range(int(input()))]
lst_p = [x for x in lst if x > 0]
lst_n = [x for x in lst if x < 0]

print(f'{lst_p}\n{lst_n}\nCount of positives: {len(lst_p)}\nSum of negatives: {sum(lst_n)}')