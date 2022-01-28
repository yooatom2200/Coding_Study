change = 1260
answer = 0

coins = [500, 100, 50, 10]

for coin in coins:
    answer += change // coin
    change %= coin

print(answer)