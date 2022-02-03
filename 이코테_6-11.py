N = int(input())
data = []
for _ in range(N):
    ins = input().split()
    data.append((ins[0], int(ins[1])))

#data.sort(key=lambda x : x[1])
data = sorted(data, key = lambda x : x[1])

for i in data:
    print(i[1], end=" ")