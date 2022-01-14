def solution(phone_book):
    test = phone_book.pop(0)
    for i in phone_book:
        if test == i[:len(test)]:
            return False
    return True