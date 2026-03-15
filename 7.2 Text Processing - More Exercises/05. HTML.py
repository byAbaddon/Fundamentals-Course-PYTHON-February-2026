for i, x in enumerate(iter(input, 'end of comments')):
    if i == 0:
        print(f'<h1>\n\t{x}\n</h1>')
    elif i == 1:
        print(f'<article>\n\t{x}\n</article>')
    else:
        print(f'<div>\n\t{x}\n</div>')