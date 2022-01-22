def solution(n, computers):
    visit = [0] * n
    answer = 0
    
    def dfs(a):
        nonlocal visit
        nonlocal computers
        nonlocal answer
        visit[a] = 1
        for i in range(n):
            if computers[a][i] == 1 and a != i:
                if visit[i] == 0:
                    dfs(i)
    
    for a in range(n):
        if visit[a] == 0:
            dfs(a)
            answer += 1
            
    return answer