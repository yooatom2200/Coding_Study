"""
전역변수(global), 전역변수아닌 함수내 변수 사용(nonlocal)
트리형식의 dfs 재귀형식 어렵다 더 공부 필요할듯
"""

def solution(numbers, target):
    answer = 0
    max_idx = len(numbers)
    
    def dfs(idx, num, tg):
        nonlocal answer
        if idx == max_idx:
            if num == tg:
                answer = answer + 1
        else:
            dfs(idx+1, num + numbers[idx], tg)
            dfs(idx+1, num - numbers[idx], tg)
            
    dfs(0, 0, target)
    return answer