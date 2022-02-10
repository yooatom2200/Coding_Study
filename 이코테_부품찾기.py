N = int(input())
product = list(map(int, input().split()))
product.sort()
M = int(input())
s_product = list(map(int, input().split()))


def bs(start, end, search):
    while start <= end:
        mid = (start + end) // 2
        if product[mid] == search:
            return "yes"
        elif product[mid] > search:
            end = mid - 1
        elif product[mid] < search:
            start = mid + 1
    return 0

for i in s_product:
    result = bs(0, N-1, i)
    if result == 0:
        print("NO", end=" ")
    else:
        print("YES", end=" ")
