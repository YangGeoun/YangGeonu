arr = [[1,1,1,0,0],
       [0,0,1,0,0],
       [0,0,1,0,0],
       [0,0,1,1,0],
       [0,0,0,1,2]]
N = 5
di = [0,0,1,-1]
dj = [1,-1,0,0]


def dfs():
    visited = [[0] * N for _ in range(N)]
    stack = [(0, 0)]
    visited[0][0] = 1
    while stack:
        ci, cj = stack[-1]
        for d in range(4):
            ni = di[d] + ci
            nj = dj[d] + cj
            if arr[ni][nj] == 2:
                return 1
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 0 and not visited[ni][nj]:
                stack.append((ni, nj))
                visited[ni][nj] = 1
                break
        else:
            stack.pop()
    return 0

print(dfs())