n, m = map(int, input().split())
trees = list(map(int, input().split()))

def bs():
    start = 0
    end = max(trees)
    saves = []
    while start <= end:
        middle = (start + end) // 2
        cuts = 0
        for i in trees:
            if i <= middle:
                cuts += 0
            else:
                cuts += i - middle
        if cuts == m:
            return middle
        elif cuts > m:
            saves.append((cuts - m, middle))
            start = middle + 1
        elif cuts < m:
            end = middle - 1
    saves.sort()
    return(saves[0][1])

print(bs())