def solve():
    for i in range(12):
        if i % 2 == 1:
            lst2[arr[i]] += 1
            cnt = 0
            for j in range(10):
                if lst2[j] > 0:
                    cnt += 1
                    if cnt > 2:
                        return 2
                else:
                    cnt = 0
                if lst2[j] == 3:
                    return 2
        else:
            lst1[arr[i]] += 1
            cnt = 0
            for j in range(10):
                if lst1[j] > 0:
                    cnt += 1
                    if cnt > 2:
                        return 1
                else:
                    cnt = 0
                if lst1[j] == 3:
                    return 1
    return 0


T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    lst1 = [0] * 10
    lst2 = [0] * 10
    print(f'#{tc} {solve()}')


