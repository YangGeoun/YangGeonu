def prim(start):
    MST = set([start])
    wieght = graph[start][:]
    wieght[start] = 0

    while len(MST) < V:
        min_weight = 0xfffffff
        min_node = -1
        for i in range(V):
            if i not in MST and wieght[i] < min_weight:
                min_weight = wieght[i]
                min_node = i
        MST.add(min_node)

        for i in range(V):
            if i not in MST and graph[min_node][i] < wieght[i]:
                wieght[i] = graph[min_node][i]
    return wieght


V, E = map(int, input().split())
graph = [[0xfffffff] * V for _ in range(V)]
for i in range(E):
    f, t, w = map(int, input().split())
    graph[f][t] = w
    graph[t][f] = w
print(prim(0))
