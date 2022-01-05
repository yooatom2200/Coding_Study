# DP 다이나믹 프로그래밍
# 한번 계산된건 반복 계산하지 않는다

def fib(a):
    if a == 0 :
        return 0
    elif a == 1 :
        return 1
    elif calc_data[a] != 0 :
        return calc_data[a]
    else :
        calc_data[a] = fib(a-1) + fib(a-2)
        return calc_data[a]

num = int(input())
calc_data = [0] * (num+1)
print(fib(num))