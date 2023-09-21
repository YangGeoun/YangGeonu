import heapq


def prim(start):
    heap = []
    # MST 에 포함되었는지 여부
    MST = [0] * V

    heapq.heappush(heap, (0, start))

    sum_weight = 0

    while heap:
        # 가장 적은 가중치를 가진 정접을 꺼냄
        weight, v = heapq.heappop(heap)

        # 이미 방문한 노드라면 pass
        if MST[v]:
            continue

        # 방문 체크
        MST[v] = 1

        sum_weight += weight

        # 갈 수 있는 노드들을 체크
        for next in range(V):
            # 갈 수 없거나 이미 방문 했다면 pass
            if graph[v][next] == 0 or MST[next]:
                continue
            heapq.heappush(heap, (graph[v][next], next))

    return sum_weight



V, E = map(int, input().split())

graph = [[0]*V for _ in range(V)]

for _ in range(E):
    f, t, w = map(int, input().split())
    graph[f][t] = w
    graph[t][f] = w
print(prim(0))