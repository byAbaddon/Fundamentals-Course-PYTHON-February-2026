k_lst = input().split(', ')
v_lst = input().split(', ')

[print(f'{k} -> {v}') for k, v in zip(k_lst, v_lst)]
