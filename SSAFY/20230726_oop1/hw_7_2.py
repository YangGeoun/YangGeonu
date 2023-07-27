# hw_7_2.py

# 아래 클래스를 수정하시오.
class StringRepeater:
    def __init__(self):
        pass
    
    @staticmethod
    def repeat_string(N,str1):
        for i in range(N):
            print(str1)

repeater1 = StringRepeater()
repeater1.repeat_string(3, "Hello")