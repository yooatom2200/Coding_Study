def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i, j in zip(participant, completion):
        print(participant)
        if i != j:
            return i
    return participant.pop()