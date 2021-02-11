N = int(input())
print(N)
board = [[0 for i in range (N)] for i in range (N)]
apple = int(input())
print(apple)
for _ in range(apple):
    x, y = map(int, input().split())

    print("x = ", x, " , y = ", y)
    