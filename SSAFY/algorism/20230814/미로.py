def miro(x, y):
    global arr
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    while True:
        for d in range(4):
            ni = x + di[d]
            nj = y + dj[d]

            if 0<= ni < N and 0 <= nj < N:
                if arr[ni][nj] == 3:
                    return 1
                if arr[ni][nj] == 0:
                    arr[x][y] = 4
                    x = ni
                    y = nj
                    break
                if arr[ni][nj] == 2:
                    arr[x][y] = 4
                    x = ni
                    y = nj
                    break
                if arr[ni][nj] == 4:
                    arr[x][y] = 1
                    x = ni
                    y = nj
                    break
        else:
            break
    return 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[int(i) for i in input()] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                x1 = i
                y1 = j

    print(miro(x1, y1))

