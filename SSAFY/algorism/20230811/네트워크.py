# DFS를 1번 진행하면 1개의 네트워크의 모든 컴퓨터를 방문할 수 있다.
# DFS를 마치고 방문하지 않은 곳에서 또 DFS를 진행한다.
# visited에 모든 요소가 1이 될때까지 DFS를 몇번 진행했는지가 네트워크의 개수이다.


def solution(n, computers):
    visited = [0] * n                  # visited를 만들ㅇ 준
    cnt = 0
    while 0 in visited:
        for i in range(len(visited)):
            if visited[i] == 0:
                stack = [i]
                visited[i] = 1
                break
        while stack:
            top = stack[-1]
            for i in range(len(computers[top])):
                if computers[top][i] == 1 and visited[i] == 0:
                    stack.append(i)
                    visited[i] = 1
                    break
            else:
                stack.pop()
        cnt += 1
    return cnt

print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))