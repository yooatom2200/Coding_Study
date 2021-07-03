'''
구간합 구하기 4
그냥 순서대로 입력받아서
조건에맞게 합쳐주면 끝
'''
import sys
n, m = map(int, sys.stdin.readline().split())
data = sys.stdin.readline().split()
print(data)

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    out = 0
    for i in range(x, y+1):#마지막 숫자까지 포함해서 더해야하므로 +1해줌
        out += int(data[i-1])#배열순번 -1
    print(out)