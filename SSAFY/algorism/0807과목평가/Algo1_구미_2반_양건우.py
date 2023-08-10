T = int(input())
for tc in range(1, T+1):
    N = int(input())                                                # 전체지역이 N x N 이다.
    x1, y1, x2, y2 = map(int, input().split())                      # 평탄화 영역에 대한 각 변수를 담는다.
    arr = [list(map(int,input().split())) for _ in range(N)]        # 전체영역 높이를 2차원 리스트에 담는다.

    sum_v = 0
    for i in range(x1, x2+1):       # 평탄화 지역의 평균을 구하기 위해 평탄화지역의 각 칸의 높이 합을 구한다.
        for j in range(y1, y2+1):
            sum_v += arr[i][j]
    avg = sum_v // ((x2-x1+1) * (y2-y1+1))  # (평단화 영역의 높이 값의 합)//(영역의 칸 수) 이다.

    cnt = 0
    for i in range(x1, x2+1):             # 현재 칸의 높이에서 평균 높이를 빼준 그 값의 절댓값의 합이 총 작업의 수이다.
        for j in range(y1, y2+1):
            temp_cnt = arr[i][j] - avg    # 모든 칸의 (칸의 현재 칸 높이) - (평균높이)을 구해준다.
            if temp_cnt < 0:              # 음수이면 양수로 바꾸어 더 할 수 있게 해준다.
                temp_cnt = -temp_cnt
            cnt += temp_cnt

    print(f'#{tc} {cnt}')
