"""
문제 조건을 항상 잘 읽기.
문제만 잘 읽었어도 풀었을 문제.
"""

N = int(input())
schedule = []
book = []
answer = 0
for _ in range(N):
    a, b = map(int, input().split())
    schedule.append([a, b])

schedule.sort(key = lambda x : x[1])
while schedule:
    pay, max_day = schedule.pop(0)
    answer += pay
    book.append([pay, max_day])
    book.sort(key = lambda x : x[0])
    if len(book) > max_day:
        answer -= book.pop(0)[0]

print(answer)