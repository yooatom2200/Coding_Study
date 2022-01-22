"""
판단의 최적화를 생각해야한다
"""
def solution(begin, target, words):
    q = [begin]
    visit = [0] * len(words)
    count = 0
    
    while True:
        count += 1
        
        tmp_q = []
        for tmp_w in q:
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
                    if words[word_index] == target:
                        return count
                    visit[word_index] = 1
                    tmp_q.append(words[word_index])
                    
        if not tmp_q :
            return 0
        q = tmp_q
        
    return count