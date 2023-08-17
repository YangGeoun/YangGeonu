# 백트래킹 기법 : 해를 찾는 도중에 막히면 되돌아가서 다시 해를 찾아 가는 기법 (가지치기)
# 최적화 문제와 결정 문제를 해결할 때 도움이 된다


# N-Queen
# 한 행에 하나의 퀸을 놓아보기
# 만약 모든 행에 퀸을 다 놓았다면 N개의 퀸을 놓은것이니 해를 찾음!
# N * N

N = 4
def solve(row):
    # row 행에 모든 열에 퀸 놓아보기
    if row == N:
        global cnt
        print('찾음')
        cnt += 1
        return

    for col in range(N):
        # row, col 에 놓을 수 있으면 퀸 놓아보기\
        if not col_check[col] and not dia_check1[row + col] \
            and not dia_check2[N-1 + row - col]:
            col_check[col] += 1
            dia_check1[row + col] += 1
            dia_check2[N-1 + row - col] += 1
            solve(row+1)    # 다음 위치로 이동
            col_check[col] -= 1
            dia_check1[row + col] -= 1
            dia_check2[N - 1 + row - col] -= 1

# 열 사용 가능여부 표시 배열
col_check = [0] * N     # 0 이면 해당 열에 퀸이 없음
# 대각선 사용 가능여부 표시 배열 만들기
dia_check1 = [0] * (2 * N - 1)      # r + c
dia_check2 = [0] * (2 * N - 1)      # (N-1) + r - c
cnt = 0

solve(0)
print(cnt)
