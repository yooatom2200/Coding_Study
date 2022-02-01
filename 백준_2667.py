"""
dfs 문제 그나마 쉬운편

"""
n = int(input())
matrix = []
visit = [[0] * n] * n
for _ in range(n):
    matrix.append(list(map(int,list(input()))))

def dfs(x,y):
    return 0