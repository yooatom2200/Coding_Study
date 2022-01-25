N = int(input())
schedule = []
for _ in range(N):
    a, b = map(int, input().split())
    schedule.append([a, b])

schedule.sort(key = lambda x : x[1])
answer, max_day = schedule.pop(-1)
count = 1
schedule.sort(key = lambda x : x[0], reverse=True)
while schedule:
    if count == max_day:
        break
    answer += schedule.pop(0)[0]
    count += 1

print(answer)