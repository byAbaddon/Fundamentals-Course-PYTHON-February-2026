matrix = [list(map(int, input().split())) for _ in range(int(input()))]
cr = input().split()

ship_destroyed = 0

while cr:
    i_r, i_c = [int(x) for x in cr.pop(0).split('-')]
    if matrix[i_r][i_c] > 0:
        matrix[i_r][i_c] = matrix[i_r][i_c] - 1
        if matrix[i_r][i_c] == 0:
            ship_destroyed += 1

print(ship_destroyed)
