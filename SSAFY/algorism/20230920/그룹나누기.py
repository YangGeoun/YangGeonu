def find_set(x):
    if teams[x] == x:
        return x

    teams[x] = find_set(teams[x])
    return teams[x]


def union(x,y):
    # 1. 이미 같은 집합인지 확인
    x = find_set(x)
    y = find_set(y)

    # 대표자가 같으니, 이미 같은 집합이다.
    if x == y:
        return
    # 2. 다른 집합이라면, 같은 대표자로 설정
    if x < y:
        teams[y] = x
    else:
        teams[x] = y
    return


T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    input_arr = list(map(int,input().split()))
    teams = [i for i in range(N)]
    for i in range(0,len(input_arr),2):
        a = input_arr[i] - 1
        b = input_arr[i+1] - 1
        union(a, b)
    ans = []
    for i in range(N):
        if find_set(i) not in ans:
            ans.append(find_set(i))
    print(teams)
    print(f'#{tc} {len(ans)}')
