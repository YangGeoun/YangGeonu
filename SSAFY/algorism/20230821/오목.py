T = int(input())
di = [1,1,1]
dj = [-1,0,1]
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    ans = 0
    for i in range(N):
        cnt1 = 0
        for j in range(N):
            if arr[i][j] == 'o':
                cnt1 += 1
                for d in range(3):
                    cnt2 = 1
                    for k in range(1, 5):
                        ni = i + k*di[d]
                        nj = j + k*dj[d]
                        if 0 <= ni < N and 0 <= nj < N:
                            if arr[ni][nj] == 'o':
                                cnt2 += 1
                            else:
                                break
                    if cnt2 == 5:
                        ans = 1
            else:
                cnt1 = 0
        if cnt1 == 5:
            ans = 1
    if ans == 1:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')