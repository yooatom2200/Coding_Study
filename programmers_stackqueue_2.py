"""
프린터문제
순서와 함께 인덱싱 해서 풀면 쉽다
"""
def solution(priorities, location):
    indexing = list(zip(priorities, range(len(priorities))))
    print(indexing)
    answer = 0
    count = 0
    while indexing:
        ma = max(indexing)
        if ma[0] == indexing[0][0]:
            count += 1
            if indexing[0][1] == location:
                answer = count
            indexing.pop(0)
        else:
            indexing.append(indexing.pop(0))
        
    return answer