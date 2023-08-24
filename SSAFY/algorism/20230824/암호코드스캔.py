import sys
sys.stdin = open("sample_input (15).txt", 'r')

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


def solve(data):
    for i in range(N):
        code = ''
        for j in range(M-1, -1, -1):
            if data[i][j] != '0':
                ni = i + 1
                while data[ni][j] == data[i][j]:
                    data[ni][j] = '0'
                    ni += 1
                if data[i][j].isdigit():
                    ten_num = int(data[i][j])
                else:
                    ten_num = ord(data[i][j]) - 55
                tmp = ''
                while ten_num:
                    tmp = str(ten_num % 2) + tmp
                    ten_num //= 2
                while len(tmp) != 4:
                    tmp = '0' + tmp
                code = tmp + code

        if code:
            keys = []
            index = len(code) - 1
            for k in range(8):
                while code[index] == '0':
                    index -= 1
                w1, w2, w3, w4 = 0, 0, 0, 0
                while code[index] == '1':
                    w4 += 1
                    index -= 1
                while code[index] == '0':
                    w3 += 1
                    index -= 1
                while code[index] == '1':
                    w2 += 1
                    index -= 1
                min_v = 10
                for el in [w2, w3, w4]:
                    if min_v > el:
                        min_v = el
                w2 = w2 // min_v
                w3 = w3 // min_v
                w4 = w4 // min_v
                w1 = 7 - w2 - w3 - w4
                keys.insert(0, code_dic[(w1,w2,w3,w4)])
            check = 0
            for i in range(8):
                if i % 2:
                    check += keys[i]
                else:
                    check += 3 * keys[i]
            if check % 10 == 0:
                sum = 0
                for el in keys:
                    sum += el
                return sum
    return 0


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(input()) for _ in range(N)]
    print(f'#{tc} {solve(data)}')