def solution(s):
    s_split = list(s)
    idx = 0
    answer = 0
    while s_split:
        if idx >= len(s_split) - 1:
            break
            
        a = s_split[idx]
        if s_split[idx] == s_split[idx+1]:
            s_split.pop(idx)
            s_split.pop(idx)
            idx = 0
        else:
            idx += 1
    
    if len(s_split) == 0:
        answer = 1

    return answer

solution(input())