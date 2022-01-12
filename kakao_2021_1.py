# 2021 카카오 인턴십 for tech developer 코테문제 1번
# 입력값에서 숫자와 문자 구분한뒤 숫자로 출력하기
# ex) 2three45sixseven -> 234567
nums = {
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9"
}
s = input()
a = []
answer = []
for i in s:
    if i.isdigit():
        answer.append(str(i))
    else:
        a.append(i)
    if "".join(a) in nums:#"".join으로 문자열로 변환
        answer.append(nums["".join(a)])
        a.clear()
print("".join(answer))