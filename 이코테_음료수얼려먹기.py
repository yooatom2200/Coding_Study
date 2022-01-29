N, M = map(int,input().split())

matrix = []
for _ in range(N):
    matrix.append(list(map(int, input())))

def dfs(x, y):
    if x < 0 or x > N-1 or y < 0 or y > M-1:
        return False
    if matrix[x][y] == 1:
        return False
    if matrix[x][y] == 0:
        matrix[x][y] = 1
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True

answer = 0
for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            answer += 1

print(answer)