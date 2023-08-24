# 먼저 2차원 배열에 입력을 받아 현재 상황을 받아 놓을 것이다.
# 2중 for문을 돌려서 탱크의 위치와 상태를 변수에 저장할 것이다.
# 나머지 동작들을 모두 코드로 구현할 것이다.

def move(dir):
    global tank_position, tank_direction
    tank_direction = dir
    ni = tank_position[0] + di[dir]
    nj = tank_position[1] + dj[dir]
    if 0 <= ni < H and 0 <= nj < W:
        if field[ni][nj] == '.':
            tank_position = [ni, nj]


di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]

T = int(input())
for tc in range(1, 1+T):
    H, W = map(int, input().split())
    field = [list(input()) for _ in range(H)]
    tank_direction = 0            # 1(상), 2(하), 3(좌), 4(우)
    tank_position = [0, 0]
    for i in range(H):
        for j in range(W):
            if field[i][j] in '^':
                tank_position = [i, j]
                tank_direction = 1
            elif field[i][j] in 'v':
                tank_position = [i, j]
                tank_direction = 2
            elif field[i][j] in '<':
                tank_position = [i, j]
                tank_direction = 3
            elif field[i][j] in '>':
                tank_position = [i, j]
                tank_direction = 4
    N = int(input())
    will_do = input()
    for el in will_do:
        if el == 'U':
            move(1)
        elif el == 'D':
            move(2)
        elif el == 'L':
            move(3)
        elif el == 'R':
            move(4)
        elif el == 'S':
            ni = tank_position[0] + di[tank_direction]
            nj = tank_position[1] + dj[tank_direction]
            while 0 <= ni < H and 0 <= nj < W:
                if field[ni][nj] == '*':
                    field[ni][nj] = '.'
                    break
                elif field[ni][nj] == '#':
                    break
                elif field[ni][nj] == '-' or field[ni][nj] == '.':
                    ni = ni + di[tank_direction]
                    nj = nj + di[tank_direction]
                else:
                    break

    for el in field:
        print(el)