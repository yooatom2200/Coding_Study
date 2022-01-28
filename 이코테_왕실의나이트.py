data = input()
y = int(data[1]) - 1
x = ord(data[0]) - ord('a')
move_x = [-2, -1, 1, 2, -2, -1, 1, 2]
move_y = [1, 2, 2, 1, -1, -2, -2, -1]
answer = 0

for a, b in zip(move_x, move_y):
    if x + a < 0 or y + b < 0 or x + a > 7 or y + b > 7:
        continue
    answer += 1

print(answer)