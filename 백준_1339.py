n = int(input())
words = []
for _ in range(n):
    words.append(input())

count = {}
for i in words:
    wlen = len(i)
    for j in i :
        if j in count:
            count[j] += 10 ** (wlen - 1)
        else:
            count[j] = 10 ** (wlen - 1)
        wlen -= 1


#print(count)
total = 0
start = 9
count = sorted(count.items(), key = (lambda x:x[1]), reverse=True)
for i in count:
    total += i[1] * start
    start -= 1

print(total)
