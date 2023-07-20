number_of_people = 0
number_of_book = 100

def increase_user():
    global number_of_people
    number_of_people += 1


def create_user(name, age, address):
    print(f'{name}님 환영합니다!')
    user_info = {'name': name, 'age': age, 'address': address}
    increase_user()
    return(user_info)


def decrease_book(num):
    global number_of_book
    number_of_book -= num // 10
    print(f'남은 책의 수 : {number_of_book}')
    pass


def rental_book(dict):
    name = dict['name']
    age = dict['age']
    decrease_book(age)
    print(f'{name}님이 {age//10}권의 책을 대여하였습니다.')
    pass


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

many_user = list(map(create_user,name,age,address))



inpo_list = list(map(lambda x: {'name' : x['name'], 'age' : x['age']}, many_user))
a = list(map(rental_book, inpo_list))


# new_list = map(lambda x : del x["address"], many_user)
# rental_book(**many_user[0])                                틀린 풀이들
# rental_book(map(lambda x : **x, many_user))


# for i in many_user:
#     del i["address"]   못풀어서 for 문으로

# for i in many_user:
#     rental_book(**i)  못풀어서 for 문으로