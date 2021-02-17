#백준 14502 연구소
import sys; r = sys.stdin.readline
from itertools import combinations
import copy
sys.setrecursionlimit(100000)
N, M = map(int, r().split())
Vt = [[*map(int,r().split())] for _ in range(N)]
ck = [[0]*M for _ in range(N)]

# DFS 바이러스가 퍼지는 것을 구현
def dfs(V, ck, x, y):
    if ck[x][y] == 0:
        ck[x][y] = 1
        if V[x][y] == 0:
            V[x][y] = 2
        # dx, dy 하는 것 보다 if로 나누면 조금 더 수행시간이 빠릅니다.
        if x+1 < N and ck[x+1][y] == 0 and V[x+1][y] != 1:
            dfs(V, ck, x+1, y)
        if x-1 >= 0 and ck[x-1][y] == 0 and V[x-1][y] != 1:
            dfs(V, ck, x-1, y)
        if y-1 >= 0 and ck[x][y-1] == 0 and V[x][y-1] != 1:
            dfs(V, ck, x, y-1)
        if y+1 < M and ck[x][y+1] == 0 and V[x][y+1] != 1:
            dfs(V, ck, x, y+1)
    return V