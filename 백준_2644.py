'''
백준_2644 촌수계산
트리처럼 생각하지말고 이웃간 계산으로 생각하면 편함
bfs적용
'''
import sys
from collections import deque
family = int(sys.stdin.readline())
p1, p2 = map(int, sys.stdin.readline().split())
num = int(sys.stdin.readline())

path = [[] for _ in range(family+1)]
visit = [0 for _ in range(family+1)]
data = [0 for _ in range(family+1)]

for _ in range(num):
    a, b = map(int, sys.stdin.readline().split())
    path[a].append(b)
    path[b].append(a)

matrix = deque()
matrix.append(p1)
visit[p1] = 1

while matrix:
    d = matrix.popleft()
    for i in path[d]:
        if visit[i] == 0:
            visit[i] = 1
            data[i] = data[d] + 1
            matrix.append(i)

print(data[p2] if data[p2] > 0 else -1)