def bfs(start):
    visited = [0] * (V+1)
    visited[start] = 1
    # 방문할 정점의 목록을 저장하는 queue
    queue = [start]
    while queue:
        front = queue.pop()
        print()
        for i in range(1, V+1):
            if adj[front][i] and visited[i] == 0:
                queue.append(i)
                visited[i] = 1


V = 7
E = 8
adj = [[0] * (V + 1) for i in range(V + 1)]
edges = list(map(int, input().split()))

for i in range(0, E*2, 2):
    adj[edges[i]][edges[i + 1]] = 1
    adj[edges[i + 1]][edges[i]] = 1

bfs(1)

