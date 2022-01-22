def dfs(begin, target, visit, words, count):
    if begin == target:
        return count
    elif sum(visit) == len(words):
        return 0
    count += 1
    begin_split = list(begin)
    almost_same = [0] * len(words)
    for i in range(len(words)):
        if visit[i] == 0:
            wds_split = list(words[i])
            for t1, t2 in zip(begin_split, wds_split):
                print(t1, t2)
                if t1 == t2 :
                    almost_same[i] += 1
    print(visit)
    print(almost_same)
    for i in range(len(almost_same)):
        if almost_same[i] == max(almost_same) and visit[i] == 0:
            dfs(words[i], target, visit, words, count)
            visit[i] = 1

def solution(begin, target, words):
    visit = [0] * len(words)
    answer = dfs(begin, target, visit, words, 0)
    return answer

            
begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
a = solution(begin, target, words)
print(a)