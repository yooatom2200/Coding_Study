'''
원의 접점을 구하는것
두 원의 중심이 같을때도 있음
내접, 외접 구분
'''

import math
T = int(input())
for i in range (0, T) :
    tmp = input().split(" ")
    x1 = float(tmp[0])
    y1 = float(tmp[1])
    r1 = float(tmp[2])
    x2 = float(tmp[3])
    y2 = float(tmp[4])
    r2 = float(tmp[5])
    
    if x1 == x2 and y1 == y2 :
        if r1 == r2 :
            print("-1")
        else :
            print("0")
    else :
        i = float(math.sqrt(math.pow(x1 - x2,2) + math.pow(y1 - y2,2)))
        if i < r1 + r2 and i > math.fabs(r2-r1) :
            print("2")
        elif i == r1 + r2 or i == math.fabs(r2-r1):
            print("1")
        else :
            print("0")