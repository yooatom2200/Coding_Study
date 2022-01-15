"""
dict함수 사용시 디폴트 출력은 key임.
value 출력을 원하면 values()를 쓰고 키값쌍으로 받아올려면 items()를 써야함
for나 in의 경우엔 key값 우선
"""
def solution(clothes):
    category = {}
    for i in clothes:
        if i[1] in category:
            category[i[1]] += 1
        else:
            category[i[1]] = 1ß
            
    rst = 1
    for i in category.values():
        rst *= (i + 1)
        
    return rst-1