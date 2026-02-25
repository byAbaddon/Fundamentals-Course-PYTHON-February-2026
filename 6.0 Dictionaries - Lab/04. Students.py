di = {}
while True:
    token = input().split(':')
    if len(token) == 1:
        for k, v in di.items():
            if token[0] in v:
                print(f'{k} - {v[token[0]]}')
        break
    else:
        name, grade, lgn = token
        if lgn == 'programming basics':
            lgn = 'programming_basics'
        di[name] = {lgn: grade}
