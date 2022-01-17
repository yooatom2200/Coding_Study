"""
효율성 검사 씹창남.. 뭐지?
heapq를 쓰면 됨
히프는 자동정렬되서 정렬시간을 단축 할 수 있음
ㅔㅐㅔ
"""
import heapq

def solution(scoville, K):
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)

    answer = 0
    while heap[0] < K:
        answer += 1
        if len(heap) < 2:
            return -1
        heapq.heappush(heap,heapq.heappop(heap) + heapq.heappop(heap) * 2)
        
    return answer