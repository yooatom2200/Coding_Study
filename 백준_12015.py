N = int(input())
nums = list(map(int, input().split()))
bigline = []
while nums:
    num = nums.pop(0)
    if num in bigline:
        continue
    bigline.append(num)

print(len(bigline))
    