a = str(input())
nums = list(map(int, list(a)))
answer = 1
for i in nums:
    if i == 0:
        continue
    answer *= i

print(answer)