from collections import deque
graph = []
N, M = input().split()
x, y = 0, 0
count = 0
for _ in range(N):
    graph.append(list(map(int,list(input()))))

def bfs():
    queue = deque()
    queue.append([x,y])
    mx = [1, -1, 0, 0]
    my = [0, 0, 1, -1]
    while queue:
        qx, qy = queue.popleft()
        for i in range(4):
            if qx + mx[i] < 0 or 
