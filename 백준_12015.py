N = int(input())
nums = list(map(int, input().split()))
bigline = []
for i in nums:
    if i in bigline:
        continue
    bigline.append(i)

print(len(bigline))