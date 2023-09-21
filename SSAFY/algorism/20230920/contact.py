for tc in range(1,11):
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    adjs = [[0]*101 for _ in range(101)]
    for i in range(0,len(arr),2):
        adjs[arr[i]][arr[i+1]] = 1
    queue = [S]
    visited = [0] * 101
    visited[S] = 1
    while queue:
        now = queue.pop(0)
        for i in range(101):
            if adjs[now][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = visited[now] + 1
    max_v = 0
    max_index = 0
    for i in range(101):
        if max_v <= visited[i]:
            max_v = visited[i]
            max_index = i

    print(f'#{tc} {max_index}')
