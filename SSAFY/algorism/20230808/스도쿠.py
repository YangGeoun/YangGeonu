# 1~9 확인
def check(x):
    tmp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for el in x:
        tmp[el] += 1
    if tmp == [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
        return 1
    else:
        return 0


# 가로 1줄 확인
def horizon(s, x):
    temp = []
    for i in range(9):
        temp.append(s[i][x])
    return check(temp)


# 세로 1줄 확인
def vertical(s, x):
    temp = []
    for i in range(9):
        temp.append(s[x][i])
    return check(temp)


# 3X3 확인
def samsam(s, x, y):
    temp = []
    for i in range(3):
        for j in range(3):
            temp.append(s[x + i][y + j])
    return check(temp)


T = int(input())
# 모든 가로줄 확인
for n in range(T):

    sudoku = [list(map(int, input().split())) for _ in range(9)]
    answer = 1

    for k in range(9):
        if horizon(sudoku, k) == 0:
            answer = 0

    # 모든 세로줄 확인
    for k in range(9):
        if vertical(sudoku, k) == 0:
            answer = 0

    # 모든 3X3 확인
    for k in range(3):
        for m in range(3):
            if samsam(sudoku, k*3, m*3) == 0:
                answer = 0

    print(f'#{n+1} {answer}')
