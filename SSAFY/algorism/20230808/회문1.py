for tc in range(1,11):
    M = int(input())
    arr = [list(input()) for _ in range(8)]
    cnt = 0
    for i in range(8):
        for j in range(9 - M):
            check = 1
            for k in range(M//2):
                if arr[i][j+k] != arr[i][M+j-k-1]:
                    check = 0
            if check == 1:
                cnt += 1

    for j in range(8):
        for i in range(9 - M):
            check = 1
            for k in range(M//2):
                if arr[i+k][j] != arr[i+M-k-1][j]:
                    check = 0
            if check == 1:
                cnt += 1

    print(f'#{tc} {cnt}')
