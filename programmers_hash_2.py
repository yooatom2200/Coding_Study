"""
sort가 중요함. sort 안하면 효율 떨어짐
접두사가 결국엔 sort시 바로 뒤에 와야됨
"""
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)):
        if i < len(phone_book) - 1:
            if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
                       return False
    return True