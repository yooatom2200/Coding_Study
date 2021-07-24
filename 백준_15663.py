'''
백준 n과 m 문제
중복수열을 걸러주는것이 중요하다
트리처럼 구성해서 따라가다 보면 정렬방법의 해답이 보임
'''

import sys
n, m = map(int, sys.stdin.readline().split())
q = list(map(int, sys.stdin.readline().split()))
q.sort()#sort 는 따로 입력해줘야함

check = [0] * n
out = []

def test(dept):
    if dept == m :
        tmp = ' '.join(map(str, out))
        print(tmp)
        return
    
    before = 0 #이전값을 비교해서 중복값을 걸러준다
    for i in range(n):
        if check[i] == 0 and before != q[i]:
            before = q[i]
            out.append(q[i])
            check[i] = 1
            test(dept+1)
            out.pop()
            check[i] = 0
        
test(0)