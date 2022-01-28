N = int(input())
act = list(input().split())
location = [1, 1]

while act:
    mission = act.pop(0)
    if mission == 'L':
        if location[1] <= 1:
            continue
        location[1] -= 1
    elif mission == 'R':
        if location[1] >= N:
            continue
        location[1] += 1
    elif mission == 'U':
        if location[0] <= 1:
            continue
        location[0] -= 1
    elif mission == 'D':
        if location[0] >= N:
            continue
        location[0] += 1

print(location)
