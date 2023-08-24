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
        for j in range(M-1,54,-1):
            if data[i][j] == 1:
                code = []
                for _ in range(8):
                    # 1의 개수 세기
                    # 0의 개수 세기
                    # 1의 개수 세기
                    # 0의 개수 구하기
                    w1, w2, w3, w4 = 0, 0, 0, 0
                    while data[i][j] == 1:
                        w4 += 1
                        j -= 1
                    while data[i][j] == 0:
                        w3 += 1
                        j -= 1
                    while data[i][j] == 1:
                        w2 += 1
                        j -= 1
                    w1 = 7 - w2 - w3 - w4
                    j -= w1
                    code.append(code_dic[(w1, w2, w3, w4)])
                return code



T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = [list(map(int, input())) for _ in range(N)]
    lst = solve(data)
    ans = 0
    for i in range(8):
        if i % 2:
            ans += 3 * lst[i]
        else:
            ans += lst[i]
    if ans % 10 == 0:
        sum = 0
        for el in lst:
            sum += el
        print(f'#{tc} {sum}')
    else:
        print(f'#{tc} 0')
