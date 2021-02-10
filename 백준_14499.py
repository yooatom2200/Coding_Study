tmp = input().split()
N ,M ,x ,y ,K = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split()))
dice = [0,0,0,0,0,0]

# 동 : 1, 서 : 2, 남 : 3, 북 : 4
for i in range(K) :
    if order[K] == 1 :
        dx = x + 1
        dy = y
    elif order[K] == 2:
        dx = x - 1
        dy = y
    elif order[K] == 3:
        dx = x
        dy = y - 1
    else:
        dx = x
        dy = y + 1

    if not 0 <= dx < N or not 0 <= dy < M:
        continue

    if order[K] == 1:
        dice[0], dice[2], dice[5], dice[3] = dice[2], dice[5], dice[3], dice[0]
    elif order[K] == 2:
        dice[0], dice[3], dice[5], dice[2] = dice[3], dice[5], dice[2], dice[0]
    elif order[K] == 3:
        dice[0], dice[4], dice[5], dice[1] = dice[4], dice[5], dice[1], dice[0]
    else:
        dice[0], dice[1], dice[5], dice[4] = dice[1], dice[5], dice[4], dice[0]

    if ground[dx, dy] == 0:
        ground[dx, dy] = dice[5]
    else:
        dice[5] = ground[dx,dy]
        ground[dx,dy] = 0

    x, y = dx, dy
    print(dice[0])