"""
배열에 삽입시키면서 풀면 쉽게 풀린다.
"""

def solution(s):
    s_split = list(s)
    a = []
    for i in s_split:
        a.append(i)
        if len(a) < 2:
            continue
        if a[-1] == a[-2]:
            a.pop()
            a.pop()

    return 1 if len(a) == 0 else 0

print(solution(input()))