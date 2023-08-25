def solve2(x,y,k):
    global home_lst
    temp_lst = home_lst[:]
    cnt = 0
    for i in range(len(temp_lst)):
        if abs(temp_lst[i][0] - x) + abs(temp_lst[i][1] - y) <= k-1:
            cnt += 1
    return cnt


T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    home_num = 0
    home_lst = []
    # 전 지역의 집의 개수 구하기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                home_num += 1
                home_lst.append([i,j])
    cost = home_num * M
    k = 1
    print(home_lst)
    solve2(2,2,5)
    # while (k*k) + (k-1) * (k-1) < cost:
    #     k += 1
    # ans = 0       # 서비스 지역 안에 집 개수가 담길 변수
    # k += 1
    # # k 일때의 비용보다 (서비스 지역 안에 집 개수 * M)이 커지면 정답이다
    # # 그래서 k 일때의 비용보다 (서비스 지역 안에 집 개수 * M)이 커질때까지 k를 줄여가며 찾아본다.
    # while (k*k) + (k-1) * (k-1) > ans * M:
    #     k -= 1
    #     max_num = 0
    #     # 모든 점에서 k 범위내의 집수를 구하고 집수의 최댓값을 구한다.
    #     for i in range(N):
    #         for j in range(N):
    #             num = solve(i,j,k)
    #             if max_num < num:
    #                 max_num = num
    #                 a = i
    #                 b = j
    #                 c = k