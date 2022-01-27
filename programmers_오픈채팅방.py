def solution(record):
    users = {}
    answer= []
    for i in record:
        line = i.split()
        if line[0] == "Enter":
            if line[1] not in users:
                users[line[1]] = line[2]
            elif line[1] in users:
                users[line[1]] = line[2]
        elif line[0] == "Change":
            users[line[1]] = line[2]
    
    for i in record:
        line = i.split()
        if line[0] == "Enter":
            answer.append(users[line[1]] + "님이 들어왔습니다.")
        elif line[0] == "Leave":
            answer.append(users[line[1]] + "님이 나갔습니다.")
    
    return answer