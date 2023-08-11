# for _ in range(10):
#     tc, E = map(int, input().split())
#     edges = list(map(int, input().split()))
#     g = [[-1] * 2 for _ in range(100)]
#     for i in range(0, E * 2, 2):
#         if g[edges[i]][0] == -1:
#             g[edges[i]][0] = edges[i+1]
#         else:
#             g[edges[i]][1] = edges[i+1]
#
#     stack = [0]
#     visited = [0] * 100
#     visited[0] = 1
#     ans = 0
#     while stack:
#         top = stack[-1]
#         for el in g[top]:
#             if el == 99:
#                 ans = 1
#             if el != -1 and visited[el] == 0:
#                 visited[el] = 1
#                 break
#         else:
#             stack.pop()
#     print(ans)


# 0(A)에서 99(B)까지 갈수 있는지
def dfs(s,e):
    stack = [s]
    visited = [0] * 100
    visited[0] = 1
    while stack:
        top = stack[-1]
        if top == 99:
            return 1
        for i in range(2):
            if adj[top][i] != -1 and visited[adj[top][i]] == 0:
                stack.append(adj[top][i])
                visited[adj[top][i]] = 1
                break
        else:
            stack.pop()
    return 0


for tc in range(1,11):
    T,E = map(int,input().split())
    edges = list(map(int,input().split()))
    adj = [[-1]*2 for _ in range(100)]

    for i in range(0,E*2,2):
        if adj[edges[i]][0] == -1:
            adj[edges[i]][0] = edges[i+1]
        else:
            adj[edges[i]][1] = edges[i+1]

    print(f'#{tc} {dfs(0,99)}')