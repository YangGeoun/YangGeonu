class Person:
    gene = "XYZ"

    def __init__(self, name):
        self.name = name
    
    def greeting(self):
        return f'안녕, {self.name}'


class Mom(Person):
    gene = 'XX'

    def __init__(self, name):
        super().__init__(name)
    
    def swim(self):
        return '엄마가 수영'
    

class Dad(Person):
    gene = 'XY'

    def __init__(self, name):
        super().__init__(name)

    def walk(self):
        return '아빠가 걷기'


class FirstChild(Dad, Mom):
    mom_gene = Mom.gene
    
    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        return '첫째가 수영'
    
    def cry(self):
        return '첫째가 응애'
    
    

baby1 = FirstChild('아가')
print(baby1.cry())
print(baby1.swim())          # Mom의 swim 덮어쓰여짐
print(baby1.walk())          # 없으면 부모로부터 받음
print(baby1.gene)            # 상속받은 순서대로 찾아보고(Dad에 gene을 보고 있으면 바로 
print(baby1.mom_gene)        # 없으면 Mom에서 gene을 봄) 정해짐
print(baby1.greeting())      # 부모의 부모 클래스에서 받아옴


print(FirstChild.mro())      # 어떤 부모 클래스를 가지는지 확인하는 메서드
                             # 변수나 메소드를 mro()의 순서대로 탐색한다.