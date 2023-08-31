T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    container.sort(reverse=True)
    truck.sort(reverse=True)
    ans = 0
    while truck:
        for j in range(len(container)):
            if truck[0] >= container[j]:
                ans += container[j]
                container.pop(j)
                truck.pop(0)
                break
        else:
            break

    print(f'#{tc} {ans}')