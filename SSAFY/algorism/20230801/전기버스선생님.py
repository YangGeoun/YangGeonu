T = int(input())

for tc in range(T):
    K, N, M = map(int, input().split())
    charge_list = list(map(int, input().split()))
    charge_list = [0] + charge_list
    charge_list = charge_list + [N]
    # 각 정류장 확인하면서 지나가는데...
    # 만약에 내가 이전 중전장에서 충전 안하고 도착하지 못하는 충전소라면
    # 이전 충전소에서 충전하기
    last = 0    # 마지막 충전소 위치
    cnt = 0
    for i in range(1, M+2):
        if charge_list[i] - charge_list[i-1] > K:    # 한번에 못가는 거리
            cnt = 0
            break
        # 아니라면 last + K 올수 있는 정류장이라면 지나침
        # 못 갈때만 이전 충전소에서 충전 (이전 정류자에서 충전했다 치자)
        if last + K < charge_list[i]:
            last = charge_list[i]
            cnt += 1
    print(f'#{tc+1} {cnt}')
