"""
종료시점 계산 중요
마지막 출력시 정수형으로 출력해주기
"""

import heapq
def solution(jobs):
    heap = []
    start, end, task, answer = -1, 0, 0, 0
    while len(jobs) > task:
        for i in jobs:
            if start < i[0] <= end:
                heapq.heappush(heap, [i[1], i[0]])
        if heap:
            tmp = heapq.heappop(heap)
            start = end
            end += tmp[0]
            answer += end - tmp[1]
            task += 1
        else :
            end += 1
            
    return int(answer / len(jobs))