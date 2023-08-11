def solution(n, computers):
    stack = [0]
    visited = [0] * n
    while stack:
        top = stack[-1]
        visited[top] = 1
        for i in range(len(computers[top])):
            if computers[top][i] == 1 and visited[top] == 0:
                stack.append(i)
                break
        else:
            stack.pop()

    answer = -1
    for el in visited:
        answer += el

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))