'''
백준 n과 m 문제
'''
import sys
n, m = map(int, sys.stdin.readline().split())
q = list(map(int, sys.stdin.readline().split())).sort()
check = [0] * n
out = []
final = []

def test(dept):
    if dept == m :
        tmp = ' '.join(map(str, out))
        if tmp not in final:
            final.append(tmp)

    for i in range(n):
        if check[i] == 0:
            out.append(q[i])
            check[i] = 1
            test(dept+1)
            out.pop()
            check[i] = 0
        
test(0)
for i in final:
    print(i)
