rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]


answer = []
idx = 1
matrix = []
for _ in range(rows):
    line = []
    for _ in range(columns):
        line.append(idx)
        idx += 1
    matrix.append(line)
    
for q in queries:
    x_min, y_min, x_max, y_max = map(lambda x : x - 1, q)
    x_now, y_now = x_min, y_min
    tmp = matrix[x_min][y_min]
    minimum = tmp if idx > tmp else idx
    for i in range(x_min, x_max):
        x_now = i+1
        print(x_now-1, y_now)
        matrix[x_now-1][y_now] = matrix[x_now][y_now]
        if matrix[x_now][y_now] < minimum:
            minimum = matrix[x_now][y_now]
    for i in range(y_min, y_max):
        y_now = i+1
        matrix[x_now][y_now-1] = matrix[x_now][y_now]
        if matrix[x_now][y_now] < minimum:
            minimum = matrix[x_now][y_now]
    for i in range(x_max, x_min, -1):
        x_now = i-1
        matrix[x_now+1][y_now] = matrix[x_now][y_now]
        if matrix[x_now][y_now] < minimum:
            minimum = matrix[x_now][y_now]
    for i in range(y_max, y_min, -1):
        y_now = i-1
        matrix[x_now][y_now+1] = matrix[x_now][y_now]
        if matrix[x_now][y_now] < minimum:
            minimum = matrix[x_now][y_now]
    matrix[x_min+1][y_min] = tmp
    answer.append(minimum)

print(answer)