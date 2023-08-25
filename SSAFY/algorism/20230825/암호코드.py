code_dic = {(3, 2, 1, 1): 0,
            (2, 2, 2, 1): 1,
            (2, 1, 2, 2): 2,
            (1, 4, 1, 1): 3,
            (1, 1, 3, 2): 4,
            (1, 2, 3, 1): 5,
            (1, 1, 1, 4): 6,
            (1, 3, 1, 2): 7,
            (1, 2, 1, 3): 8,
            (3, 1, 1, 2): 9
            }

htob = {
'0' : '0000',
'1' : '0001',
'2' : '0010',
'3' : '0011',
'4' : '0100',
'5' : '0101',
'6' : '0110',
'7' : '0111',
'8' : '1000',
'9' : '1001',
'A' : '1010',
'B' : '1011',
'C' : '1100',
'D' : '1101',
'E' : '1110',
'F' : '1111'
}

def solve()
    result = 0
    for i in range(N):
        j = M * 4 -1
        while j > 54:
            # 암호코드가 시작하는지 확인
            if binary_data[i][j] == '1' and binary_data[i-1][j] == 0:
                code = []
                for _ in range(8):
                    w1,w2,w3,w4 = 0,0,0,0
                    while binary_data[i][j] == '1':
                        w4 += 1
                        j -= 1
                    while binary_data[i][j] == '0':
                        w3 += 1
                        j -= 1
                    while binary_data[i][j] == '1':
                        w2 += 1
                        j -= 1
                    rate = min(w2,w3,w4)
                    w2 //= rate
                    w3 //= rate
                    w4 //= rate
                    w1 = 7-(w2+w3+w4)
                    j -= w1*rate
                    code.append(code_dic[(w1,w2,w3,w4)])
                odd_num = 0
                even_num = 0
                for el in code:
                    if el % 2:
                        odd_num += el
                    else:
                        even_num += el

                if (odd_num * 3 + even_num) % 10 == 0:
                    result += odd_num + even_num
            j -= 1
    return result

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    binary_data = [''for _ in range(N)]

    for i in range(N):
        for j in range(M):
            binary_data[i] += htob[data[i][j]]

    # 뒤에서부터 읽어오면서 ... 암호코드 찾기

            j -= 1