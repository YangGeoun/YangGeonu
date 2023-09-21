def dijkstra(start):
    weight = graph[start][:]
    selected = set()
    weight[start] = 0
    while len(selected) < N+1:
        min_weight = 0xfffffff
        min_node = -1
        for i in range(N+1):
            if i not in selected and min_weight > weight[i]:
                min_weight = weight[i]
                min_node = i
        selected.add(min_node)

        for i in range(N+1):
            if weight[i] > min_weight + graph[min_node][i]:
                weight[i] = min_weight + graph[min_node][i]
    return weight


T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    graph = [[0xfffffff]*(N+1) for _ in range(N+1)]
    for i in range(E):
        s, e, w = map(int, input().split())
        graph[s][e] = w

    print(f'#{tc}',dijkstra(0)[-1])
