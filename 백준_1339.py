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



total = 0
start = 9
count = sorted(count, reverse=True)
for i in total:
    print(i)
            
