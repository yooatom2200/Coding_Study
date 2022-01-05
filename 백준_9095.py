def fib(a):
    if a == 1:
        return 1
    elif a == 2:
        return 2
    elif a == 3:
        return 4
    elif triple[a] != 0:
        return triple[a]
    triple[a] = fib(a-1) + fib(a-2) + fib(a-3)
    return triple[a]

count = int(input())
triple = [0] * 11
for _ in range(count):
    print(fib(int(input())))
