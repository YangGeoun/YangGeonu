import requests
from pprint import pprint as print

# # 무작위 유저 정보 요청 경로
# API_URL = 'https://jsonplaceholder.typicode.com/users/1'
# # API 요청
# response = requests.get(API_URL)
# # JSON -> dict 데이터 변환
# parsed_data = response.json()

# # 응답 데이터 출력
# print(response)

# # 변환 데이터 출력
# print(parsed_data)
# # 변환 데이터의 타입
# print(type(parsed_data))

# # 특정 데이터 출력
# print(parsed_data['name'])
# print(parsed_data['username'])
# print(parsed_data['company']['name'])

black_list = ['Hoeger LLC', 'Keebler LLC', 'Yost and Sons', 'Johns Group', 'Romaguera-Crona']
consord_user_list = dict()


def create_user(list):                                       #블랙리스트에 없는 기업 사람만 리스트에 추가 하는 함수
    for dict in list:                                        #dummy_list의 각각의 사람 딕셔너리를 반복
        company = dict['company']                            #company와 name을 쓰기 편하게 변수에 담음
        name = dict['name']
        if censorship(dict):                                 #블랙리스트에 있는 기업인지 없는 censorship()함수가 판별(없으면 : True, 있으면 : False)
            temp_name_list = []                              #이름을 리스트에 담으라고 요구사항에 적혀있어 임시 이름 리스트를 만듬
            temp_name_list.append(name)                      #비어있는 임시 이름 리스트에 이름을 넣는다
            consord_user_list[company] = temp_name_list      #consord_user_list 딕셔너리에 company라는 이름의 key로 하고
    pass                                                     #valuetemp_name_list를 value로 하는 요소 추가   ('회사이름' : [이름])

def censorship(dict):                                        #블랙리스트에 있는 기업인지 확인하는 함수
    company = dict['company']                                #company와 name을 쓰기 편하게 변수에 담음
    name = dict['name']
    if company in black_list:                                     #company가 black_list안에 있다면 아래 코드 실행
        print(f'{company}소속의 {name}은/는 등록할 수 없습니다.')   
        return False
    else:                                                         #company가 black_list안에 없다면(else) 아래 코드 실행
        print('이상 없습니다.')
        return True

dummy_data = []

for i in range(10):
    API_URL = 'https://jsonplaceholder.typicode.com/users/'+str(i+1)    # 10개의 사람들 데이터를 받아오는 코드
    response = requests.get(API_URL)
    parsed_data = response.json()
    company = parsed_data['company']['name']                             #쓰기 편하게 각 변수에 데이터를 담는다
    lat = parsed_data['address']['geo']['lat']
    lng = parsed_data['address']['geo']['lng']
    name = parsed_data['name']
    temp_dict = {'company' :company , 'lat':lat, 'lng':lng, 'name':name}   #임시 딕셔너리를 만들고        
    if -80 < float(lat) < 80 and -80 < float(lng) < 80:                    # 위도경도가 -80초과, 80미안 인지 확인하고
        dummy_data.append(temp_dict)                                       # dummy_data 리스트에 데이터를 담는다.
        


#   보기 안 좋아서 위에 코드로 변경(변수에 담아서 코드작성하니 깔끔)
#   temp_dict = {'company' :parsed_data['company']['name'] , 'lat':parsed_data['address']['geo']['lat'], 'lng':parsed_data['address']['geo']['lng'], 'name':parsed_data['name']}
#   if -80 < float(parsed_data['address']['geo']['lat']) < 80 and -80 < float(parsed_data['address']['geo']['lng']) < 80:
#       dummy_data.append(temp_dict)

create_user(dummy_data)                       
                            
print(consord_user_list)