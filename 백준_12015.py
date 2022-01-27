"""
lower bound 써야된대..
첨보는데 일단 알아보고 해보자
"""
N = int(input())
nums = list(map(int, input().split()))
bigline = []
for i in nums:
    if i in bigline:
        continue
    bigline.append(i)

print(len(bigline))