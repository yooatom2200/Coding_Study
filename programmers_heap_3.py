"""
정확도만 평가해서 뭐...
max나 min 쓸때 빈 큐가 아닌지 확인하고 사용
근데 이방식은 힙을 제대로 쓴게 아니라 잘 모르겠따
"""

import heapq

def solution(operations):
    h = []
        
    for i in operations:
        a, b = i.split(" ")
        if a == "I":
            heapq.heappush(h,int(b))
        elif a == "D" and len(h) > 0:
            if b == "1":
                h.sort(reverse=True)
                heapq.heappop(h)
                h.sort()
            elif b == "-1":
                heapq.heappop(h)
            
    if h: 
        return [max(h),h[0]]
    else: 
        return [0, 0]