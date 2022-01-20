"""
문제 진짜 생각 많이해야된다
문제를 이해 못해서 못풀었다.
"""

def solution(citations):
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i] <= i:
            return i

    return len(citations)