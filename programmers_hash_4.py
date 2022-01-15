"""
dict랑 tuple 생각 잘 해야됨
key로 sort할건지, value로 sort할건지
접근 방식도 숙지하기. dict 호출시 output은 key.
"""
def solution(genres, plays):
    categories = {}
    categories_idx = {}
    answer = []
    k = 0
    for i, j in zip(genres, plays):
        if i in categories:
            categories[i] += j
            categories_idx[i].append((j , k))
        else:
            categories[i] = j
            categories_idx[i] = [(j, k)]
        k += 1
        
    categories = sorted(categories.items(), key = lambda x : x[1], reverse=True)
    for i in categories_idx:
        categories_idx[i] = sorted(categories_idx[i], key = lambda x : x[0], reverse=True)
        
    for i in categories:
        f = categories_idx[i[0]]
        answer.append(f[0][1])
        if len(f) >= 2:
            answer.append(f[1][1])
            
    return answer