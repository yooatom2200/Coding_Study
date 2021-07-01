import sys
n, m = map(int, sys.stdin.readline().split())
matrix = [sys.stdin.readline().rstrip() for _ in range(n)]
visit = [[0] * m for _ in range(n)]
visit[0][0] = 1
queue = [(0,0)]

while queue:
    x, y = queue.pop(0)
    if x == n-1 and y == m-1:
        #print(visit)
        print(visit[x][y])

    if x+1 < n and matrix[x+1][y] == '1' and visit[x+1][y] == 0:
        visit[x+1][y] = visit[x][y] + 1
        queue.append((x+1, y))
    if y+1 < m and matrix[x][y+1] == '1' and visit[x][y+1] == 0:
        visit[x][y+1] = visit[x][y] + 1
        queue.append((x, y+1))
    if x-1 >= 0 and matrix[x-1][y] == '1' and visit[x-1][y] == 0:
        visit[x-1][y] = visit[x][y] + 1
        queue.append((x-1, y))
    if y-1 >= 0 and matrix[x][y-1] == '1' and visit[x][y-1] == 0:
        visit[x][y-1] = visit[x][y] + 1
        queue.append((x, y-1))
