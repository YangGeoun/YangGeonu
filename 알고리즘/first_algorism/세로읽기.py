matrix_in = []
length = 0

for i in range(5):
    temp_list = list(input())
    if length < len(temp_list):
        length = len(temp_list)
    matrix_in.append(temp_list)



for j in range(length):
    for i in range(5):
        try:
            print(matrix_in[i][j],end='')
        except:
            continue
# 입력 받은 5줄의 string(문자열)의 길이가 달라서 
# 에러가 발생 -> 예외처리로 해결

# matrix의 초기 설정을 빈 리스트가 아닌 
# *과 같은 특수문자로 가득 채워놓고 
# if 문을 활용하여 *일때 contine로도 가능할 거같다.