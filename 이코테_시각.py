N = int(input())
time = (N * 60 + 59) * 60 + 59
answer = 0
while time:
    hour = (time // 60) // 60
    minuit = (time - hour * 3600) // 60
    sec = time - hour * 3600 - minuit * 60
    text_time = str(hour) + str(minuit) + str(sec)
    if "3" in text_time:
        answer += 1
    time -= 1

print(answer)