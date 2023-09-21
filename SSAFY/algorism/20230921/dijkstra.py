# 내가 갈 수 있는 경로 중 누적거리가 제일 짧은 것부터 고르자

import heapq


def dijkstra(start):
    # 2. 우선순위 큐
    pq = []
    # 출발점 추가
    heapq.heappush(pq, (0,start))
    distance[start] = 0

    while pq:
        # 누적 거리가 가장 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(pq)

        # 이미 방문한 지점 + 누적 거리가 더 짧게 방문한 적이 있다면 pass
        if distance[now] < dist:
            continue

        # 인접 노드를 확인
        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            # next_node 로 가기 위한 누적 거리
            new_cost = dist + cost

            # 누적 거리가 기존보다 크네?
            if distance[next_node] <= new_cost:
                continue
            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))


n, m = map(int, input().split())
graph = [[] for i in range(n)]
for _ in range(m):
    f, t, w = map(int, input().split())
    graph[f].append([t, w])

# 1. 누적 거리를 계속 저장
INF = int(1e9)
distance = [INF] * n
dijkstra(0)
print(distance)


