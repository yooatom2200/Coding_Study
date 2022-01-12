n = int(input())
numbers = []
alphabet = []
for i in range(n):
    numbers.append(input())

numbers.sort(key=len, reverse=True)
for i in range(len(numbers), 0, -1):
    if(numbers[i-1])