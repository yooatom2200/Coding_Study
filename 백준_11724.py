'''
간선문제
dfs나 bfs로 탐색하여 연결요소를 구한다
'''

import sys
sys.setrecursionlimit(10000)#재귀함수 제한 1000회에서 증가

def dfs(v):#깊이우선탐색
    visit[v] = True
    for g in graph[v]:
        if not visit[g]:
            dfs(g)

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]#간선들 입력될 그래프
visit = [False for _ in range(n+1)]#해당노드 방문여부
count = 0#연결요소 카운트

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    if not visit[i]:
        dfs(i)
        count += 1

print(count)
