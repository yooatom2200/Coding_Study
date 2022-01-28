N, M = map(int, input().split())
answer = 0

for _ in range(N):
    tmp = list(map(int, input().split()))
    if answer < min(tmp):
        answer = min(tmp)
    
print(answer)