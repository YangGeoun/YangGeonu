import heapq


def dijkstra(start_i, start_j):
    heap = []
    heapq.heappush(heap, (0, start_i, start_j))
    value = [[0xffffffffff] * N for _ in range(N)]
    value[start_i][start_j] = 0
    while heap:
        w, gi, gj = heapq.heappop(heap)
        if value[gi][gj] < w:
            continue
        else:
            for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                tempi = gi + di
                tempj = gj + dj
                if 0 <= tempi < N and 0 <= tempj < N:
                    newcost = w + 1 + abs(case[gi][gj] - case[tempi][tempj])
                    if value[tempi][tempj] <= newcost:
                        continue
                    else:
                        value[tempi][tempj] = newcost
                        heapq.heappush(heap, (newcost, tempi, tempj))
    return value


T = int(input())
for t in range(T):
    N = int(input())
    case = [list(map(int, input().split())) for _ in range(N)]
    result = dijkstra(0, 0)
    for i in result:
        print(i)
