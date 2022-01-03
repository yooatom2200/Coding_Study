N, M = map(int, input().split())
many = list(map(int,input().split()))[1:]
partyCount = 0

for _ in range(M):
    inData = list(map(int,input().split()))
    inData = inData[1:]
    checkIn = 0

    for i in inData:
        if i in many:
            checkIn = 1

    if checkIn == 1:
        for i in inData:
            many.append(i)
            many = list(set(many))
    else:
        partyCount += 1

print(partyCount)
