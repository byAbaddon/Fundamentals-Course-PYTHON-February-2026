matrix = [input().split() for _ in range(int(input()))]

rows = len(matrix)
cols = len(matrix[0])

visited = [[False]*cols for _ in range(rows)]

def dfs(r, c):
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return 0
    if visited[r][c] or matrix[r][c] != '.':
        return 0

    visited[r][c] = True
    count = 1

    count += dfs(r+1, c)
    count += dfs(r-1, c)
    count += dfs(r, c+1)
    count += dfs(r, c-1)

    return count

best = 0

for r in range(rows):
    for c in range(cols):
        if matrix[r][c] == '.' and not visited[r][c]:
            best = max(best, dfs(r, c))

print(best)
