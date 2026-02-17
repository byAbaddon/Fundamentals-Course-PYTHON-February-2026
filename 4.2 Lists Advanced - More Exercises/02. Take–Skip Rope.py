string, str_result, index = '', '', 0
e_lst, o_list = [], []

for x in input():
    if x.isdigit():
        if index & 1:
            o_list.append(int(x))
        else:
            e_lst.append(int(x))
        index += 1
    else:
        string += x

for i, c in enumerate(string):
    e = o = None
    if e_lst:
        e = e_lst.pop(0)
        str_result += string[:e]
    if o_list:
        o = o_list.pop(0)
        string = string[e + o:]

print(str_result)
