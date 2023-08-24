T = int(input())
for tc in range(1, T+1):
    cnt = 0
    N = int(input())
    arr = [input() for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            detal_x = -(N//2) + i
            detal_y = -(N//2) + j
            if detal_x < 0:
                detal_x = -detal_x
            if detal_y < 0:
                detal_y = -detal_y
            if detal_y + detal_x <= N//2:
                ans += int(arr[i][j])
    print(f'#{tc} {ans}')