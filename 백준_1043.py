N, M = map(int, input().split())
known = list(map(int,input().split()))[1:]
parties = list()
partyTrue = [0] * M
isVisit = [0] * N

for i in known:
    isVisit[i-1] = 1



for _ in range(M):
    parties.append(list(map(int, input().split()))[1:])

while known:
    guest = known.pop()
    include = set()
    for partyIdx in range(M):
        party = set(parties[partyIdx])
        if guest in party:
            include = include.union(party)
            partyTrue[partyIdx] = 1

    for i in include:
        if not isVisit[i - 1]:
            known.append(i)
            isVisit[i - 1] = 1

print(partyTrue.count(0))
