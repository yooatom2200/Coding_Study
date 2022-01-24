N = int(input())
meeting = []
for _ in range(N):
    i, j = map(int, input().split())
    meeting.append([i, j])

print(meeting)
print("-")
meeting.sort(key = lambda x : x[0])
print(meeting)
print("-")
meeting.sort(key = lambda x : x[1])
print(meeting)
print("-")

finish = 0
answer = 0
for i, j in meeting:
    if i >= finish:
        finish = j
        answer += 1

print(answer)