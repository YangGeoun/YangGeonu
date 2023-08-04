def cnt_charge():
    position = 0
    cnt = 0
    if charge_list[0] > K:
        return 0
    for i in range(len(charge_list) - 1):
        if K < charge_list[i + 1] - charge_list[i]:
            return 0
    idx = 0
    while position < N - K:
        for i in range(K + position, position, -1):
            if i in charge_list:
                position = i
                cnt += 1
                break
    return cnt


T = int(input())
for tc in range(T):
    K, N, M = map(int, input().split())
    charge_list = list(map(int, input().split()))
    print(f'#{tc + 1} {cnt_charge()}')




