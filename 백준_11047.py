'''
동전문제
지정한 가격만큼 동전의 최소개수를 구하기
각 배열을 나눈값의 인덱스 0을 찾고
이후 이전인덱스값부터 나눠주기 시작해서
각 값을 더해주면 완성
'''
import sys
n, k = map(int,sys.stdin.readline().split())
coin = []
index = 0
result = 0

for _ in range(n):
    coin.append(int(sys.stdin.readline()))
coin.reverse()

for i in range(n):
    if int(k / coin[i]) > 0:
        index = i
        break

while k > 0:
    result += int(k / coin[index])
    k = k % coin[index]
    index += 1

print(result)
    