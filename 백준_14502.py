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

    # 안전지대와 바이러스의 위치를 파악합니다.
zeros = []
virus = []
for i in range(N):
    for j in range(M):
        if Vt[i][j] == 0:
            zeros.append((i,j))
        if Vt[i][j] == 2:
            virus.append((i,j))

# 벽을 세우는 부분
def blocking(Vx, ck, zeros):
    # comination 조합에 따라 벽을 세움
    for i, j in coms:
        Vx[i][j] = 1
    # 바이러스가 퍼짐
    for i, j in virus:
        Vx = dfs(Vx, ck, i, j)
    # 안전지대의 수 세기
    cnt = 0
    for i in range(N):
        for j in range(M):
            if Vx[i][j] == 0 : cnt+=1
    return cnt

    max_zero = 0
# 순열조합을 활용하여 벽을 막을 수 있는 경우를 모두 고려
# 해당 부분이 비효율적인 경향이 있음
for coms in combinations(zeros, 3):
    # 값이 변하면 안되므로 deepcopy()를 활용
    # copy 모듈을 사용할 수 없다면 
    # [v for v in Vt]와 같은 방식을 활용할 수 있음
    V_in = copy.deepcopy(Vt)
    cks = copy.deepcopy(ck)
    x = blocking(V_in, cks, coms)
    max_zero = max(max_zero, x)
print(max_zero)