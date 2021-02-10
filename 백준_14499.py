N ,M ,x ,y ,K = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split()))
dice = [0,0,0,0,0,0]

# 동 : 1, 서 : 2, 북 : 3, 남 : 4
for i in range(K) :
    if order[i] == 1 :
        dx = x
        dy = y + 1
    elif order[i] == 2: 
        dx = x
        dy = y - 1
    elif order[i] == 3:
        dx = x - 1
        dy = y
    else:
        dx = x + 1
        dy = y

    if not 0 <= dx < N or not 0 <= dy < M:
        continue

    if order[i] == 1:
        dice[0], dice[3], dice[5], dice[2] = dice[3], dice[5], dice[2], dice[0]
    elif order[i] == 2:
        dice[0], dice[2], dice[5], dice[3] = dice[2], dice[5], dice[3], dice[0]
    elif order[i] == 3:
        dice[0], dice[4], dice[5], dice[1] = dice[4], dice[5], dice[1], dice[0]
    else:
        dice[0], dice[1], dice[5], dice[4] = dice[1], dice[5], dice[4], dice[0]

    if ground[dx][dy] == 0:
        ground[dx][dy] = dice[5]
    else:
        dice[5] = ground[dx][dy]
        ground[dx][dy] = 0

    x, y = dx, dy
    print(dice[0])