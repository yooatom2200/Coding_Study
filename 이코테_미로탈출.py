from collections import deque
matrix = []
N, M = map(int,input().split())
count = 0
for _ in range(N):
    matrix.append(list(map(int,list(input()))))

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    mx = [1, -1, 0, 0]
    my = [0, 0, 1, -1]
    while queue:
        pops = queue.popleft()
        qx, qy = pops[0], pops[1]
        for i in range(4):
            if qx + mx[i] < 0 or qx + mx[i] >= N or qy + my[i] < 0 or qy + my[i] >= M:
                continue
            if matrix[qx][qy] == 0:
                continue
            if matrix[qx+mx[i]][qy+my[i]] == 1:
                queue.append([qx+mx[i], qy+my[i]])
                matrix[qx+mx[i]][qy+my[i]] = matrix[qx][qy] + 1
    
    print(matrix)
    return matrix[-1][-1]

print(bfs(0,0))

