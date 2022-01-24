N = int(input())
time_line = input()
times = list(map(int, time_line.split()))
times.sort(key = lambda x : x)
answer = 0
acc_time = 0
for i in times:
   acc_time = acc_time + i
   answer += acc_time 

print(answer)