"""
bfs로 풀어야된다... dfs 재귀로 하면 넘나 깊어지나?
또 나왔다... 깊은복사 조심하기
"""
def bfs(begin, target, words):
    q = [begin]
    visit = [0] * len(words)
    count = 0
    while True:
        if target in q:
            return count
        elif sum(visit) == len(words):
            return 0
        
        tmp_q = [i for i in q]
        q = []
        for tmp_w in tmp_q:
            if tmp_w == target:
                return count
            tmp_list = list(tmp_w)
            for word_index in range(len(words)):
                same_count = 0
                word_list = list(words[word_index])
                for i, j in zip(word_list, tmp_list):
                    if i == j :
                        same_count += 1
                if same_count == len(target) - 1 and visit[word_index] == 0:
                    visit[word_index] = 1
                    q.append(words[word_index])
        count += 1

def solution(begin, target, words):
    return bfs(begin, target, words)
 
begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
a = solution(begin, target, words)
print(a)