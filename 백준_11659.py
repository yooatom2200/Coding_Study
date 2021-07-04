'''
구간합 구하기 4
그냥 순서대로 입력받아서
조건에맞게 합쳐주면 끝인줄 알았지만 시간초과...
구간합은 미리 해당구간의 합을 구해놓고 계산해주면 더 빠르게 작동 가능
'''
import sys
sys.setrecursionlimit(10000000)#재귀함수 제한 1000회에서 증가
n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
sum = [0]#구간합 저장소

for i in range(n):
    sum.append(sum[i] + data[i])#구간합 계산

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    print(sum[y] - sum[x-1])#합이 큰쪽의 구간합에서 합이 작은쪽의 구간합을 빼면 원하는값 나온다