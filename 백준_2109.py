N = int(input())
schedule = []
for _ in range(N):
    a, b = map(int, input().split())
    schedule.append([a, b])

schedule.sort(key = lambda x : x[0], reverse=True)
schedule.sort(key = lambda x : x[1])


answer = 0
day = 0

for i in schedule:
    if i[1] > day:
        day = i[1]
        answer += i[0]

print(answer) if N != 0 else print(0)