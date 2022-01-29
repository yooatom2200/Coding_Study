N, M = map(int, input().split())
x, y, view = map(int, input().split())

matrix = []
count = 0
gone = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))
    gone.append(list(map(lambda x : 1 - x, matrix[-1])))

move_x = [0, 1, 0, -1]#북동남서
move_y = [-1, 0, 1, 0]#0123

while True:
    if matrix[x][y] == 0:
        matrix[x][y] = 1
        count += 1
    if view == 0:
        view = 3
        if matrix[x+move_x[view]][y+move_y[view]] == 1:
            continue
    elif view == 3:
        view = 2
        if matrix[x+move_x[view]][y+move_y[view]] == 1:
            continue
    elif view == 2:
        view = 1
        if matrix[x+move_x[view]][y+move_y[view]] == 1:
            continue
    elif view == 1:
        view = 0
        if matrix[x+move_x[view]][y+move_y[view]] == 1:
            continue
    