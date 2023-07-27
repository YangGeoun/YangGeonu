# ws_7_2py

# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
    
    def print_info(self):
        print(f'Width: {self.width}')
        print(f'Height: {self.height}')
        print(f'area: {self.calculate_area()}')
        print(f'perimeter: {self.calculate_perimeter()}')


shape1 = Shape(5, 3)
shape1.print_info()
