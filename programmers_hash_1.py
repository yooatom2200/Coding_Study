def solution(participant, completion):
    for i in completion:
        if i in participant:
            participant.remove(i)
            
    answer = str(participant[0])
    return answer