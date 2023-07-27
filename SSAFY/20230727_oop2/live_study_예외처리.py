# 잘못된 입력 예외처리(숫자입력)
# try:
#     str_in = input('숫자입력:')
#     num = int(str_in)
# except ValueError:
#     print(f"{str_in}은(는) 숫자가 아닙니다.")



# 잘못된 입력 예외처리(나눌 값 입력)
try:
    str_in = input('100을 나눌 값을 입력하시오 : ')
    num = int(str_in)
    print(100/num)
except ValueError:
    print(f"{str_in}은(는) 숫자가 아닙니다.")
except ZeroDivisionError:
    print(f"0으로 나눌 수 없습니다.")
except:
    print('에러가 발생하였습니다.')