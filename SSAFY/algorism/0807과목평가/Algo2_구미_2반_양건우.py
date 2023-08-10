T = int(input())

for tc in range(1, 1+T):
    N = int(input())                              # 총 리스트의 길이를 받는다.
    arr = list(map(int, input().split()))         # 각 칸의 데이터를 리스트 형식으로 받는다.

    step = 1                              # 튕기는 거리에 대한 변수이다.
    ans = 0                               # 모든 점수들의 합이 담길 변수이다.
    while step <= N:                      # step 이 1 ~ N까지  아래의 코드를 반복해준다.
        sum = 0                           # step 만큼 튕기면서 얻은 점수가 들어갈 변수이다.
        for i in range(0, N, step):       # step 에 맞는 칸의 합을 구하기 위한 반복문
            sum += arr[i]
        ans += sum                        # 각 step 의 점수를 ans 에 더해준다.
        step += 1                         # 한 번의 챌린지가 끝나면 스탭을 키워준다.

    if ans < 0:                           # 만약 획득 점수가 0점 이하인 경우는 0점으로 출력합니다
        ans = 0

    print(f'#{tc} {ans}')
