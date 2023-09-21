T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr.pop(0)
    edgs = [[0] * N for i in range(N)]
    cnt = 0
    for i in range(N-1):
        for j in range(i+1,i+arr[i]+1):
            if j > N-1:
                continue
            edgs[j][i] = 1
    for i in edgs:
        print(i)
    queue = [N-1]
    visited = [100] * N
    visited[N-1] = 0
    while queue:
        now = queue.pop(0)
        if now == 0:
            break
        for i in range(N-1):
            if edgs[now][i] == 1:
                queue.append(i)
                if visited[i] > visited[now] + 1:
                    visited[i] = visited[now] + 1
        cnt += 1
    print(visited)