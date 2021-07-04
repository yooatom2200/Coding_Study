'''
동전문제
지정한 가격만큼 동전의 최소개수를 구하기
'''
import sys
n, k = map(int,sys.stdin.readline().split())
coin = []

for _ in range(n):
    coin.append(int(sys.stdin.readline()))
coin.reverse()
print(coin)