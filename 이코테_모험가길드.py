N = input()
people = list(map(int, input().split()))
answer = 0
people.sort()
for i in people:
    for _ in range(i):
        people.pop()
    answer += 1

print(answer)