"""
이전 2번문제보다 선녀같다.
약수들을 구해서 절반 자르고 약수들 통해 공식 구하고
큰값먼저 출력하면 끝.
"""

def solution(brown, yellow):
    total = brown + yellow
    numlist = []
    for i in range(1,total+1):
        if total % i == 0:
            numlist.append(i)
    numlist = numlist[:len(numlist)+1]
    for i1 in numlist:
        i2 = total / i1
        tmp = i1 * 2 + (i2 - 2) * 2
        if tmp == brown and total - tmp == yellow:
            return [i1, i2] if i1 > i2 else [i2, i1]