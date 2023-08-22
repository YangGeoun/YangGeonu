T = int(input())
for tc in range(1, 1+T):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    ads = [[] for _ in range(E + 2)]
    for i in range(0, 2 * E, 2):
        ads[arr[i]].append(arr[i+1])
    stack = [N]
    visited = [0] * (E + 2)
    while stack:
        now = stack[-1]
        for el in ads[now]:
            if visited[el] == 0:
                stack.append(el)
                visited[el] = 1
                break
        else:
            stack.pop()
    ans = 1
    for el in visited:
        ans += el
    print(f'#{tc} {ans}')