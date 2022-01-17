"""
효율성 검사 씹창남.. 뭐지?
"""
def solution(scoville, K):
    answer = 0
    while min(scoville) < K:
        answer += 1
        scoville.sort()
        if len(scoville) < 2:
            return -1
        scoville.append(scoville.pop(0) + (scoville.pop(0) * 2))
        
    return answer