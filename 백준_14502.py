#백준 14502 연구소
#지도 입력
N, M = map(int, input().split())
area = [[0 for _ in range (N)] for _ in range (M)]
for i in range (N):
    area[i] = map(int, input().split())

