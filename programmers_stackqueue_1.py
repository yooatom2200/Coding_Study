def solution(progresses, speeds):
    answer = []
    count = []
    for i, j in zip(progresses, speeds):
        empty = 100 - i
        if empty % j > 0:# 소수점으로 떨어질때 +1
            count.append((empty // j) + 1)
        else:
            count.append((empty // j))
    
    day = 0
    jobs = 0
    
    while count:
        if count[0] <= day:
            count.pop(0)
            jobs += 1
        else:
            if jobs > 0 :
                answer.append(jobs)
                jobs = 0
            day += 1
    answer.append(jobs)
        
    return answer