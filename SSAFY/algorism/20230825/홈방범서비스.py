# 홈방범 서비스를 가장 많은 집들에 제공하는 서비스 영역을 찾았는 문제이다
# 모든 집이 서비스 영역 안에 있을때의 비용을 계산해서 최대 비용을 찾는다
# 최대 비용일때 손해를 보는지 확인 손해보지 않는 영역이 있으면 그때가 답이다.
# 모든 영역 손해를 본다면 비용을 줄여가면서 모든 영역을 탐색하여 이익을 보는 순간이 답이다.



# 다이아몬드 모양 안에 1의 개수를 구하는 함수
# 다이아몬드 모양의 중앙을 가로로 갈라서
# 위로 뾰족한 삼각형모양 아래로 뾰족한 삼각형모양으로 나누어 계산
def solve(x,y,k):
    cnt = 0
    # 위로 뾰족한 삼각형모양의 1 개수 구하기
    for i in range(k):                 # 중앙을 포함하여 위로 k번 올라가면서 계산할 것이다.
        for j in range(2*k-1-2*i):     # 각 줄에서 2*k-1-2*i 번 확인할 것이다
            ni = x+i                   # ni의 좌표는 i가 1증가할때 위로 1 증가한다.
            nj = y-(k-1)+i+j           # nj의 좌표는 y-(k-1)+i에서 시작해서 오른쪽으로 j만큼 확인할 것이다.
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == 1:
                    cnt += 1
    # 아래로 뾰족한 삼각형모양의 1 개수 구하기
    for i in range(k-1):               # 중앙이 비포함이므로 아래로 k-1번 내려가면서 계산할 것이다.
        for j in range(2*k-3-2*i):     # 각 줄에서 2*k-3-2*i 번 확인할 것이다
            ni = x-1-i                 # ni의 좌표는 x-1에서 시작해서 i가 1증가할때 아래로 1 감소한다.
            nj = y-(k-2)+i+j           # nj의 좌표는 y-(k-2)+i에서 시작해서 오른쪽으로 j만큼 확인할 것이다.
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == 1:
                    cnt += 1
    return cnt


def solve2(x,y,k):
    cnt = 0
    for i in range(len(home_lst)):
        if abs(home_lst[i][0] - x) + abs(home_lst[i][1] - y) <= k-1:
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
    # 모든 집의 비용을 이용해서 최대 K 값 구하기
    while (k*k) + (k-1) * (k-1) < cost:
        k += 1
    ans = 0       # 서비스 지역 안에 집 개수가 담길 변수
    k += 1
    # k 일때의 비용보다 (서비스 지역 안에 집 개수 * M)이 커지면 정답이다
    # 그래서 k 일때의 비용보다 (서비스 지역 안에 집 개수 * M)이 커질때까지 k를 줄여가며 찾아본다.
    while (k*k) + (k-1) * (k-1) > ans * M:
        k -= 1
        max_num = 0
        # 모든 점에서 k 범위내의 집수를 구하고 집수의 최댓값을 구한다.
        for i in range(N):
            for j in range(N):
                num = solve2(i,j,k)
                if max_num < num:
                    max_num = num
        ans = max_num
    print(f'#{tc} {ans}')
