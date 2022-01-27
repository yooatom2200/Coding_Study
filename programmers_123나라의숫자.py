"""
숫자를 마지막에 재정렬 시켜주는것까지가 정답.
"""
def solution(n):
    answer = ''
    while n:
        if n % 3:
            answer += str(n % 3)
            n //= 3
        else:
            answer += "4"
            n = n//3 - 1
    return answer[::-1]