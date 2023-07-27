class Character:
    def __init__(self,name,hp,force,depence):
        self.name = name
        self.hp = hp
        self.force = force
        self.depence = depence

    def atack(self, taget):
        taget.hp -= self.force - taget.depence
        print(f'{self.name}이(가) {taget.name}을(를) 공격하였습니다')
        print(f'{taget.name}의 hp가 {taget.hp}이(가) 되었습니다.')


class Monster:
    count = 0
    
    @classmethod
    def num_of_monster(cls):
        print(f'총 몬스터 수는{cls.count}마리 입니다.')

    def __init__(self,name,hp,force,depence):
        self.name = name
        self.hp = hp
        self.force = force
        self.depence = depence
        Monster.count += 1
    
    def atack(self, taget):
        taget.hp -= self.force - taget.depence
        print(f'{self.name}이(가) {taget.name}을(를) 공격하였습니다')
        print(f'{taget.name}의 hp가 {taget.hp}이(가) 되었습니다.')

A = Character('용사',100,100,30)

B = Monster('슬라임',80,35,20)
C = Monster('고블린',70,50,50)
D = Monster('트롤',40,40,20)
E = Monster('드래곤',50,70,50)

print(E.name)
