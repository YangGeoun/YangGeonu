#상속  (코드 재사용, 계층 구조, 유지보수의 용이성)
class Person:
    def __init__(self, name, age):
            self.name = name
            self.age = age

    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')

class Professor(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department

class Studunt(Person):
    def __init__(self, name, age, gpa):
        super().__init__(name, age)
        self.gpa = gpa


s1 = Studunt('김학생', 23, 3.5)
s1.talk()

p1 = Professor('박교수', 59,'컴퓨터공학과')
p1.talk()