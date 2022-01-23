n = int(input())
matrix = []
visit = [[0] * n] * n
for _ in range(n):
    line = list(input())
    line = list(map(int, line))
    matrix.append(line)
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                dfs(matrix, visit)

def dfs(matrix, visit):
    return 0

print(matrix)