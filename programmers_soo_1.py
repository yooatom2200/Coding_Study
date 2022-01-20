def solution(answers):
    answer = []
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    a1,a2,a3 = 0, 0, 0
    for i in range(len(answers)):
        if i == 0:
            if p1[0] == answers[0]:
                a1 += 1
            if p2[0] == answers[0]:
                a2 += 1
            if p3[0] == answers[0]:
                a3 += 1
            continue
        if p1[i % len(p1)] == answers[i]:
            a1 += 1
        if p2[i % len(p2)] == answers[i]:
            a2 += 1
        if p3[i % len(p3)] == answers[i]:
            a3 += 1
        
    mint = max(a1, a2, a3)
    if a1 == mint:
        answer.append(1)
    if a2 == mint:
        answer.append(2)
    if a3 == mint:
        answer.append(3)
    return answer