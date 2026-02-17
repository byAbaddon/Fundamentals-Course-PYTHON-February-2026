def dfs(r, c, moves):
    global best

    if r < 0 or c < 0 or r >= n or c >= m or maze[r][c] != ' ':
        return

    if (r in (0, n-1) or c in (0, m-1)):
        best = max(best, moves + 1)
        return

    maze[r][c] = 'v'

    dfs(r, c-1, moves+1)
    dfs(r-1, c, moves+1)
    dfs(r, c+1, moves+1)
    dfs(r+1, c, moves+1)

    maze[r][c] = ' '


n = int(input())
maze = []
sr = sc = 0

for i in range(n):
    row = list(input())
    for j, ch in enumerate(row):
        if ch == 'k':
            sr, sc = i, j
            row[j] = ' '
    maze.append(row)

m = len(maze[0])
best = -1

dfs(sr, sc, 0)

print(f'Kate got out in {best} moves" if best != -1 else "Kate cannot get out')
