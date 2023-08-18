T = 10
for tc in range(1,T + 1):
    t = int(input())
    arr = [list(map(int, input())) for _ in range(100)]

    di = [-1,1,0,0]
    dj = [0,0,-1,1]
    ans = 0
    stack = [(1, 1)]
    visited = [[0] * 100 for i in range(100)]
    while stack:
        x, y = stack[-1]
        if arr[x][y] == 3:
            ans = 1
            break
        for d in range(4):
            ni = x + di[d]
            nj = y + dj[d]
            if 0 <= ni < 100 and 0 <= nj < 100:
                if arr[ni][nj] != 1 and visited[ni][nj] == 0:
                    stack.append((ni, nj))
                    visited[ni][nj] = 1
                    break
        else:
            stack.pop()

    print(f'#{tc} {ans}')