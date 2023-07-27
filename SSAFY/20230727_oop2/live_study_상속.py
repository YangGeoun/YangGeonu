#상속  (코드 재사용, 계층 구조, 유지보수의 용이성)

class Professor:
    def __init__(self, name, age, department):
        self.name = name                         #코드 반복
        self.age = age                           #코드 반복
        self.department = department 

    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')     #코드 반복

class Studunt:
    def __init__(self, name, age, gpa):
        self.name = name                          #코드 반복
        self.age = age                            #코드 반복
        self.gpa = gpa
        
    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')      #코드 반복


s1 = Studunt('김학생', 23, 3.5)
s1.talk()

p1 = Professor('박교수', 59,'컴퓨터공학과')
p1.talk