import copy
N = int(input())
half_N = float(N) / 2
matrix = [[0] * N for _ in range(N)]
for i in range(N):
    HT = list(input())
    for j in range(len(HT)):
        if HT[j] == 'T':
            matrix[i][j] = 1

matrix_a = copy.deepcopy(matrix)
matrix_b = copy.deepcopy(matrix)
#가로열 변화시 비교
for i in range(N):
    compare_a = 0
    compare_b = 0
    for j in range(N):
        compare_a += matrix_a[i][j]
        compare_b += matrix_b[j][i]

    if compare_a > half_N:
        for j in range(N):
            matrix_a[i][j] = 1 - matrix_a[i][j]

    if compare_b > half_N:
        for j in range(N):
            matrix_b[j][i] = 1 - matrix_b[j][i]

a = sum(sum(matrix_a, []))
b = sum(sum(matrix_b, []))
print(a) if a <= b else print(b)