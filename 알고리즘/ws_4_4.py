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
dummy_data = []

def create_user(list):
    for dict in list:
        company = dict['company']
        name = dict['name']
        if censorship(dict):
            temp_name_list = []
            temp_name_list.append(name)
            consord_user_list[company] = temp_name_list
    pass

def censorship(dict):
    company = dict['company']
    name = dict['name']
    if company in black_list:
        print(f'{company}소속의 {name}은/는 등록할 수 없습니다.')
        return False
    else:
        print('이상 없습니다.')
        return True


for i in range(10):
    API_URL = 'https://jsonplaceholder.typicode.com/users/'+str(i+1)
    response = requests.get(API_URL)
    parsed_data = response.json()
    company = parsed_data['company']['name']
    lat = parsed_data['address']['geo']['lat']
    lng = parsed_data['address']['geo']['lng']
    name = parsed_data['name']
    temp_dict = {'company' :company , 'lat':lat, 'lng':lng, 'name':name}           
    if -80 < float(lat) < 80 and -80 < float(lng) < 80:
        dummy_data.append(temp_dict)
        print(dummy_data)

#   temp_dict = {'company' :parsed_data['company']['name'] , 'lat':parsed_data['address']['geo']['lat'], 'lng':parsed_data['address']['geo']['lng'], 'name':parsed_data['name']}
#   if -80 < float(parsed_data['address']['geo']['lat']) < 80 and -80 < float(parsed_data['address']['geo']['lng']) < 80:
#       dummy_data.append(temp_dict)

create_user(dummy_data)
print(consord_user_list)