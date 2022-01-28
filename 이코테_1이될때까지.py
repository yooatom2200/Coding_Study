N, K = map(int, input().split())
answer = 0
while N:
    another = N % K
    mok = N // K if N > K else 0
    answer += another
    if mok > 1:
        answer += 1
    N //= K

print(answer)
