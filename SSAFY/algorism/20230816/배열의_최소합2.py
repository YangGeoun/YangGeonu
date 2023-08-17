def minselect(i,N,s):
    global minsum
    if s > minsum:
        return
    if i == N:
        if minsum > s:
            minsum = s
    else:
        for j in range(N):
            if selected[j] == 0:
                lst[j] = arr[i][j]
                selected[j] = 1
                minselect(i+1,N,s+arr[i][j])
                lst[j] = 0
                selected[j] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minsum = 100
    lst = [0] * N
    selected = [0] * N
    minselect(0,N,0)
    print(f'#{tc} {minsum}')