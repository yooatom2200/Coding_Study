N, M = map(int, input().split())
matrix_a = []
matrix_b = []
for _ in range(N):
    matrix_a.append(list(map(int, list(input()))))
for _ in range(N):
    matrix_b.append(list(map(int, list(input()))))

answer = 0
for i in range(N-2):
    for j in range(M-2):
        if matrix_a[i][j] != matrix_b[i][j]:
            for k in range(3):
                for l in range(3):
                    matrix_a[i+k][j+l] = 1 - matrix_a[i+k][j+l]
            answer += 1

if matrix_a == matrix_b:
    print(answer)
else:
    print(-1)