import heapq

T = int(input())
for tc in range(1, 1+T):
    N, M, X = map(int, input().split())
    arr = [[] for _ in range(N+1)]
    arr2 = [[] for _ in range(N+1)]
    for i in range(M):
        x, y, c = map(int, input().split())
        arr[x].append((c, y))
        arr2[y].append((c, x))
    distance = [0xfffffff] * (N+1)
    distance2 = [0xfffffff] * (N+1)
    pq = []
    heapq.heappush(pq, (0,X))
    set_a = set()
    while len(set_a) < N:
        min_w, min_node = heapq.heappop(pq)
        set_a.add(min_node)
        if distance[min_node] < min_w:
            continue
        distance[min_node] = min_w
        for el in arr[min_node]:
            w, t = el
            if t not in set_a:
                heapq.heappush(pq, (min_w + w, t))

    pq = []
    heapq.heappush(pq, (0, X))
    set_a = set()
    while len(set_a) < N:
        min_w, min_node = heapq.heappop(pq)
        set_a.add(min_node)
        if distance2[min_node] < min_w:
            continue
        distance2[min_node] = min_w
        for el in arr2[min_node]:
            w, t = el
            if t not in set_a:
                heapq.heappush(pq, (min_w + w, t))
    ans = [0] * (N+1)
    for j in range(1, len(arr)):
        ans[j] = distance[j] + distance2[j]

    print(f'#{tc} {max(ans)}')