"""
효율성 통과를 위해 두 배열을 정렬한 뒤
zip으로 하나씩 호출하고 비교후 다른게 있으면 p에서 출력
전부 통과하면 마지막 인원이 검거된것이므로 마지막사람 추출을 위해 pop 진행
"""
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i, j in zip(participant, completion):
        print(participant)
        if i != j:
            return i
    return participant.pop()