N, M = map(int, input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort(reverse=True)
answer, count = 0, 0

for a ,b in zip(A, B):
    if a < b and count < M:
        answer += b
        count += 1
    else:
        answer += a

print(answer)
