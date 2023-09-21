import heapq

T = int(input())

di = [-1,1,0,0]
dj = [0,0,-1,1]

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0xfffffff] * N for _ in range(N)]
    queue = [(0,0,0)]
    set_a = set()
    while queue:
        w, x, y = heapq.heappop(queue)
        set_a.add((x, y))
        if visited[x][y] <= w:
            continue
        visited[x][y] = w
        for d in range(4):
            nx = x + di[d]
            ny = y + dj[d]
            if 0 <= nx < N and 0 <= ny < N:
                if (nx, ny) not in set_a:
                    z = 0
                    if arr[nx][ny] > arr[x][y]:
                        z = arr[nx][ny] - arr[x][y]
                    heapq.heappush(queue,(w+1+z, nx, ny))

    print(f'#{tc}', visited[N-1][N-1])