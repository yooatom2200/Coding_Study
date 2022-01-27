"""
점화식을 잘 세우면 금방 풀리는 문제이다.
최대공약수는 math의 gcd를 이용하면 된다.
"""

from math import gcd

def solution(w,h):
    g = gcd(w,h)
    a = w/g
    b = h/g
    cancel = (a + b - 1) * g
    answer = w * h - cancel
    return answer