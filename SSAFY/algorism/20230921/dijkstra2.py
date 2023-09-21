# 내가 갈 수 있는 경로 중 누적거리가 제일 짧은 것부터 고르자


def dijkstra(start):
    weight = graph[start][:]
    selected = set()
    weight[start] = 0
    while len(selected) < V:
        min_weight = 0xfffffff
        min_node = -1
        for i in range(V):
            if i not in selected and weight[i] < min_weight:
                min_weight = weight[i]
                min_node = i
        selected.add(min_node)

        for i in range(V):
            if i not in selected:
                if weight[i] > min_weight + graph[min_node][i]:
                    weight[i] = min_weight + graph[min_node][i]
    return weight


V, E = map(int, input().split())
graph = [[0xfffffff]*V for i in range(V)]

for _ in range(E):
    f, t, w = map(int, input().split())
    graph[f][t] = w

print(dijkstra(0))