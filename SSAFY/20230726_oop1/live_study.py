# 클래스 정의
class Person:
    # 속성(변수)
    blood_color = 'red'       # 클래스 변수 모든 인스턴스들이 공유하는 변수
    
    # 메서드                   # 생성자 메서드  
    def __init__(self, name): # 인스턴스를 생성하고 필요한 초기값을 설정드
        self.name = name      # 인스턴스 변수 : 인스턴스마다 독립적인 값을 가지며 생성될 때마다 초기화됨
                              
    def singing(self):
        return f'{self.name}가 노래합니다.'  #인스턴스 메서드 
    
# 인스턴스 생성
singer1 = Person('iu')
singer2 = Person('BTS')

# 메서드 호출
print(singer1.singing())
print(singer2.singing())

# 속성(변수) 접근
print(singer1.blood_color)