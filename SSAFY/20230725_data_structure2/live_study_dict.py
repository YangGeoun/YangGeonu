# dict 메서드

d = {'a' : 1, 'b': 1, 'c': 1, 'd': 1} 
print(d)

d.clear()           #모든 요소 제거
print(d)
d = {'a' : 1, 'b': 2, 'c': 3, 'd': 4} 

print(d.get('a'))               # 값을 가져오는 메서드 d['a']와 같다.
print(d.get('e','UnKnown'))     # 값이 없으면 None 또는 내가 원하는 값 반환 가능
#print(d['e'])                  # d['a']는 키가 없으면 에러 KeyError: 'e'

print(d.keys())                 # 딕셔너리의 모든 키 반환 dict_keys(['a', 'b', 'c', 'd'])
for key in d.keys():            # 리스트처럼 반복가능
    print(key)

print(d.values())               # 딕셔너리의 모든 밸류 반환 dict_values([1, 2, 3, 4])
for value in d.values():        # 리스트처럼 반복가능
    print(value)

print(d.items())                # 키와 밸류가 한쌍인 튜플 리스트를 반환
for key,value in d.items():
    print(key, value)

print(d.pop('d'))               # 해당하는 키의 벨류를 반환하고 요소 제거
print(d)
#print(d.pop('e'))              # 키가 없으면 에러 KeyError: 'e'
print(d.pop('e',"'e' 키는 없어요")) # 키가 없을 때, 원하는 값 반환가능

print(d.setdefault('a'))      #키와 연결된 값을 반환
print(d.setdefault('a', 5))
print(d.setdefault('e', 5)) #키가 없으면 default와 연결한 키를 딕셔너리에 추가하고 default 반환
print(d)          

d1 = {'d' : 4, 'e': 100, 'f' : 6} 
d.update(d1)             #키와 벨류 없으면 추가 있으면 덮어쓰기
print(d)                 #여러개 한번에 업데이트 가능
d.update(e = 5)
print(d)
d.update(g = 7)
print(d)
d.update(h = 8, i =9)
print(d)