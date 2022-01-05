# DP 다이나믹 프로그래밍
# 한번 계산된건 반복 계산하지 않는다

#num = input()
def fib(a):
    if a == 0 :
        return 0
    elif a == 1 :
        return 1
    elif calc_data[a] != 0 :
        return calc_data[a]
    else :
        calc_data[a] = calc_data[a-1] + calc_data[a-2]
        return calc_data[a]

calc_data = [0] * 90
print(fib(input()))
