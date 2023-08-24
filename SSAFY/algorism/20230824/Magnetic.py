# 빨간색 밑에 파란색이 있다면 교착상태가 된다.
# 파란색이 밑에 있는 빨간색의 수를 세면 그 수가 교착상태의 갯수이다.
T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for j in range(N):
        for i in range(N):
            if arr[i][j] == 1:
                for k in range(i+1, N):
                    if arr[k][j] == 1:
                        break
                    if arr[k][j] == 2:
                        cnt += 1
                        break
    print(f'#{tc} {cnt}')

