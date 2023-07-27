# ws_8_1.py

# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0

    def __init__(self):
        Animal.num_of_animal += 1
    

class Dog(Animal):
    sound = '멍멍'

    def __init__(self):
        super().__init__()
    
    def bark(self):
        print('멍멍!')

class Cat(Animal):
    sound = '야옹'
    
    def __init__(self):
        super().__init__()

    def meow(self):
        print('야옹!')

class Pet(Dog,Cat):
    
    def __init__(self,sound):
        super().__init__()
        self.sound = sound
    
    def make_sound(self):
        print(self.sound)
    
    def play(self):
        print('애완동물과 놀기')

    @classmethod
    def access_num_of_animal(cls):
        return f'동물의 수는 {Animal.num_of_animal}마리 입니다.'
    
    def __str__(self):
        return f'애완동물은 {super().sound} 소리를 냅니다.'
    

pet = Pet('그르르')
print(pet)

