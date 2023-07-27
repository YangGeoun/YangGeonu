# set 메서드 

s = {1,2,3,4,5}
print(s)

s.add(6)         # 항목 추가, 있으면 변화 없음
print(s)

s.clear()        # 모든 항목 제거
print(s)         #출력결과 set() 이다. 만약 {}라면 딕셔너리랑 겹쳐서
s = {'김싸피','이싸피','박싸피','양싸피','홍싸피'}

# s.remove(3)      # 항목 제거, 없으면 Key error
print(s) 

print(s.pop())   # 임의항목 반환하고 제거
print(s)         # 임의 하는 의미는 해시테이블 참고 공부필요
                 # 정수값은 해시값 고정 문자는 해시값 변함
                 # 정수값 자체가 해시값
s = {1,2,3,4,5}
s1 = {1,2,3,4,5}
s.update([4,5,6,7,8])
print(s)
s2 = {4,5,6,7,8}
s1 = {1,2,3,4,5}

print(s1.difference(s2))    #차집합
print(s1.intersection(s2))  #교집합
print(s1.issubset(s))       #s1이 s에 포함
print(s1.issuperset(s))     #s가 s1에 포함
print(s1.union(s2))         #합집합

