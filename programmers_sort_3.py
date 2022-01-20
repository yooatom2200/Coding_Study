"""
문제 진짜 생각 많이해야된다
문제를 이해 못해서 못풀었다.
이해전 테스트는 내가 이해한대로 되었지만
모든 테스트케이스는 통과 못했다.
"""

def solution(citations):
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i] <= i:
            return i

    return len(citations)