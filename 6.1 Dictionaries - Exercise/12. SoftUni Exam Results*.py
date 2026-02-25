di_usr = {}
di_lng = {}

for token in iter(input, 'exam finished'):
    if 'banned' not in token:
        name, lng, pts = token.split('-')
        di_lng[lng] = di_lng.setdefault(lng, 0) + 1
        di_usr.setdefault(name, []).append(int(pts))

    else:
        name, _ = token.split('-')
        if name in di_usr:
            del di_usr[name]

print('Results:')
[print(k, '|', max(v)) for k, v in di_usr.items()]
print('Submissions:')
[print(k, '-', v) for k, v in di_lng.items()]
