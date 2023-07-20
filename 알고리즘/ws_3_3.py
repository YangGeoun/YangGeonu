import book 

def rental_book(name, num):
    book.decrease_book(num)
    print(f'{name}님이 {num}권의 책을 대여하였습니다.')
    pass

rental_book('홍길동', 3)