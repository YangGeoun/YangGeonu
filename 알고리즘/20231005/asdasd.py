T = int(input())
di = [-1,1,0,0]
dj = [0,0,-1,1]


def dfs(x,y,num):
    if len(num) == 7:
        set_a.add(num)
        return
    for d in range(4):
        ni = x + di[d]
        nj = y + dj[d]
        if 0 <= ni < 4 and 0 <= nj < 4:
            dfs(ni,nj,num + arr[ni][nj])


for tc in range(1,T+1):
    arr = [list(input().split()) for _ in range(4)]
    set_a = set()
    for i in range(4):
        for j in range(4):
            dfs(i,j,arr[i][j])
    print(f'#{tc} {len(set_a)}')