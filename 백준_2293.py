# DP는 점화식이 제일 중요
# 1원 동전의 경우 모든 숫자에 대해 1개의 경우만 생성
# n원 동전의 경우 숫자 - n원부터 생성가능
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
