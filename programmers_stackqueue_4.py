"""
파이썬 리스트를 그냥 복사할 경우 깊은복사가 진행된다
주소까지 싹 공유되기에 얕은복사를 원할경우 .copy()를 사용하면 된다
효율성 테스트 통과 필요 -> deque 사용
"""
from collections import deque

def solution(prices):
    p_deq = deque(prices)
    answer = []
    
    while p_deq:
        a = p_deq.popleft()
        tmp = 0
        for i in p_deq:
            tmp += 1
            if a > i:
                break
        answer.append(tmp)
                
    return answer