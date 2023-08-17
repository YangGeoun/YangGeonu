def rotate1(origin): # 원본 받아서 90도회전한 배열 반환
    new_mat = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            new_mat[c][N-1-r] = origin[r][c]
    return new_mat


def rotate2(arr):
    new_arr = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_arr[i][j] = arr[N-1-j][i]

    return new_arr


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    mat = [input().split() for _ in range(N)]

    print(rotate1(mat))
    print(rotate2(mat))