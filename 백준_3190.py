from collections import deque

#뱀. 머리좌표, 꼬리좌표
hx, hy = 0, 0
tx, ty = 0, 0
snake = deque([[hx, hy]])
turn = "r"

#보드크기, 뱀 = 1, 사과 = 2. 빈공간 = 0
N = int(input())
board = [[0 for i in range (N)] for i in range (N)]
board[hx][hy] = 1

#사과개수, 위치설정
apple = int(input())
for i in range(apple):
    aX, aY = map(int, input().split())
    board[aX - 1][aY - 1] = 2

#뱀 방향변환 정보
L = int(input())
tX = [0 for _ in range(L)]
tC = [0 for _ in range(L)]
for i in range(L):
    tmp = input().split()
    tX[i] = int(tmp[0])
    tC[i] = tmp[1]

time = 1
while(True):
    #머리이동
    if turn == "r":
        hy = hy + 1
    elif turn == "l":
        hy = hy - 1
    elif turn == "u":
        hx = hx - 1
    else:
        hx = hx + 1

    #머리가 보드 밖으로 진출시
    if not 0 <= hx < N or not 0 <= hy < N:
        break

    #머리 위치한곳 확인(빈곳 or 사과 or 몸통)
    if board[hx][hy]  == 0:
        board[hx][hy] = 1
        snake.append([hx,hy])
        tx, ty = snake.popleft()
        board[tx][ty] = 0
    elif board[hx][hy] == 2:
        board[hx][hy] = 1
        snake.append([hx,hy])
    else:
        break

    #뱀 방향전환
    for i in range(L):
        if tX[i] == time:
            if turn == "r" and tC[i] == "D":
                turn = "d"
            elif turn == "r" and tC[i] == "L":
                turn = "u"
            elif turn == "l" and tC[i] == "D":
                turn = "u"
            elif turn == "l" and tC[i] == "L":
                turn = "d"
            elif turn == "u" and tC[i] == "D":
                turn = "r"
            elif turn == "u" and tC[i] == "L":
                turn = "l"
            elif turn == "d" and tC[i] == "D":
                turn = "l"
            elif turn == "d" and tC[i] == "L":
                turn = "r"
    time = time + 1

print(time)

