'''
백준_2644 촌수계산
'''
import sys
from collections import deque
family = int(sys.stdin.readline())
p1, p2 = map(int, sys.stdin.readline().split())
num = int(sys.stdin.readline())

path = [[] for _ in range(num)]
visit = [0 for _ in range(num)]
data = [0 for _ in range(num)]

for _ in range(num):
    a, b = map(int, sys.stdin.readline().split())
    path[a].append(b)
    path[b].append(a)

def bfs(start, end):
    matrix = deque()
    matrix.append(start)
    visit[start-1] = 1
    while matrix:
        data = matrix.pop()
        for i in path(data):
            if visit[i-1] == 0:
                matrix.append(i)
                visit[i-1] == 1
                data[i-1] = data[i] + 1
            
            if i == end:
                print(data[i-1])
                break
    print(-1)


bfs(p1, p2)