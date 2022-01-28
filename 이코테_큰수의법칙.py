"""
좀 더 수학적으로 접근해보기
식을 세워서 하면 시간은 더 단축됨
"""
N, M, K  = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort(reverse=True)
big = nums[0]
n_big = nums[1]

answer = (K * big + n_big) * (M // (K + 1)) + big * (M % (K + 1))

print(answer)