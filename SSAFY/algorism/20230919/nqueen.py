# N * N 크기의 행렬애 N개의 퀸을 놓아보기
# row번 행에 퀸 하나 놓기
def nqueen(row):
    global cnt
    if row == N:
        # for i in board:
        #     print(i)
        # print()
        cnt += 1
        return
    # 모든 열에 일단 놓아보고, 놓아지면, 놓고 다음 행 놓으러 가기
    for i in range(N):
        # i번 열에 퀸 놓아보기
        if selected[i] == 0 and row-i not in sub and row+i not in add:
            sub.append(row-i)
            add.append(row+i)
            board[row][i] = 1
            selected[i] = 1
            nqueen(row+1)
            board[row][i] = 0
            selected[i] = 0
            sub.remove(row-i)
            add.remove(row+i)


N = 4
board = [[0]*N for _ in range(N)]
selected = [0] * N
add = []
sub = []
cnt = 0
nqueen(0)
print(cnt)