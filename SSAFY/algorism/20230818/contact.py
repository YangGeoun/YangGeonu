T = 10
for tc in range(1, 1 + T):
    N, start = map(int, input().split())
    arr = list(map(int, input().split()))
    contact = [[] for _ in range(101)]
    for i in range(0, N, 2):
        contact[arr[i]].append(arr[i+1])
    q = [start]
    visited = [0] * 101
    while q:
        now = q.pop(0)
        for el in contact[now]:
            if visited[el] == 0:
                visited[el] = visited[now] + 1
                q.append(el)
    max = 0
    max_index = 0
    for i in range(101):
        if max <= visited[i]:
            max = visited[i]
            max_index = i
    print(f'#{tc} {max_index}')

