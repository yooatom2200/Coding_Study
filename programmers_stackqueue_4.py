"""
파이썬 리스트를 그냥 복사할 경우 깊은복사가 진행된다
주소까지 싹 공유되기에 얕은복사를 원할경우 .copy()를 사용하면 된다
"""
def solution(prices):
    answer = [0] * len(prices)
    idx = 0
    while prices:
        a = prices.pop(0)
        for i in prices:
            answer[idx] += 1
            if a > i:
                break
        idx += 1
                
    return answer