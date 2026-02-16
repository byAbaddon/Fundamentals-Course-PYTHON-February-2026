board = [input().split() for _ in range(3)]
lines = [
    *board,                              # h
    *zip(*board),                        # v
    [board[i][i] for i in range(3)],     # d
    [board[i][2 - i] for i in range(3)]  # ad
]

for line in lines:
    if len(set(line)) == 1 and line[0] != '0':
        print('First player won' if line[0] == '1' else 'Second player won')
        exit()
print('Draw!')
