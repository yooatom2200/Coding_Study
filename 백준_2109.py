N = int(input())
schedule = []
book = []
for _ in range(N):
    a, b = map(int, input().split())
    schedule.append([a, b])

schedule.sort(key = lambda x : x[1])
print(schedule)
while schedule:
    pay, max_day = schedule.pop(0)
    book.append([pay, max_day])
    book.sort(key = lambda x : x[0])
    if len(book) > max_day:
        print(book.pop(0), max_day)

print(book)