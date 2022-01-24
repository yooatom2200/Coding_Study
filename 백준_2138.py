"""
변수 하나 하나 꼼꼼히 살펴라 제발
최종 결정이 될 요소들을 기준으로 변경점을 잡고 진행하면
쉽게 풀 수 있다.
"""

N = int(input())
before = list(map(int,list(input())))
before_2 = before.copy()
after = list(map(int,list(input())))
answer = 0
answer_2 = 0

for i in range(N):
    if i == 0:
        before[0] = 1 - before[0]
        before[1] = 1 - before[1]
        answer += 1
    elif i == N-1 and before[i-1] != after[i-1]:
        before[i-1] = 1 - before[i-1]
        before[i] = 1 - before[i]
        answer += 1
    elif before[i-1] != after[i-1]:
        before[i-1] = 1 - before[i-1]
        before[i] = 1 - before[i]
        before[i+1] = 1 - before[i+1]
        answer += 1

for i in range(N):
    if i == 0:
        continue
    elif i == N-1 and before_2[i-1] != after[i-1]:
        before_2[i-1] = 1 - before_2[i-1]
        before_2[i] = 1 - before_2[i]
        answer_2 += 1
    elif before_2[i-1] != after[i-1]:
        before_2[i-1] = 1 - before_2[i-1]
        before_2[i] = 1 - before_2[i]
        before_2[i+1] = 1 - before_2[i+1]
        answer_2 += 1

if before == after and before_2 == after:
    print(min(answer,answer_2))
elif before == after:
    print(answer)
elif before_2 == after:
    print(answer_2)
else:
    print(-1)