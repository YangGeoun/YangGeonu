dr = [-1,0,1,0]
dc = [0,1,0,-1]

def dfs(r,c,visited):
    global cnt
    stack = [(r,c)]
    visited[r][c] = 1
    while stack:
        r , c = stack[-1]
        if miro[r][c] == 3:
            cnt -= 1
            return cnt
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0<=nr<N and 0<=nc<N and miro[nr][nc] != 1 and visited[nr][nc] == 0:
                stack.append((nr,nc))
                cnt += 1
                visited[nr][nc] = 1
                break
        else :
            stack.pop()
            cnt -= 1

    return 0   # 길못찾으면


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    miro = [list(map(int,input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                si,sj = i,j

    visited = [[0]*N for _ in range(N)]
    cnt = 0
    ans = dfs(si,sj,visited)
    print(f'#{tc} {ans}')