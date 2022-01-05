a, b = map(int, input().split())
coin = []
num = [0] * (b+1)
num[0] = 1
for _ in range(a):
    coin.append(int(input()))

for i in coin:
    for j in range(i, b+1):
        num[j] += num[j-i]

print(num[b])
