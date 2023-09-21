def solve(num):
    visited = [0] * 1000001
    queue = [num]
    visited[num] = 1

    while queue:
        now = queue.pop(0)
        if now == M:
            return visited[M]
        if 1 <= now*2 <= 1000000:
            if not visited[now*2]:
                queue.append(now*2)
                visited[now*2] = visited[now] + 1
        if 1 <= now+1 <= 1000000:
            if not visited[now+1]:
                queue.append(now+1)
                visited[now+1] = visited[now] + 1
        if 1 <= now-1 <= 1000000:
            if not visited[now-1]:
                queue.append(now-1)
                visited[now-1] = visited[now] + 1
        if 1 <= now-10 <= 1000000:
            if not visited[now-10]:
                queue.append(now-10)
                visited[now-10] = visited[now] + 1



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    print(f'#{tc}',solve(N)-1)