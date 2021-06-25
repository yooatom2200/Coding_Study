#2Xn 타일링
#점화식으로 문제 접근해야댐. 2->2, 3->3, 4->5, 5->8, 6->13
#n번째 데이터는 n-1과 n-2번째 데이터의 합(2와 3은 제외)
#출력은 경우의수에서 10007을 나눈 나머지값을 출력
num = int(input())
if num <= 3:
    print(num % 10007)
else:
    data = [0 for _ in range(num+1)]#배열초기화
    data[1] = 1
    data[2] = 2
    for i in range(3,num+1):
        data[i] = data[i-1] + data[i-2]
    print(data[num] % 10007)

