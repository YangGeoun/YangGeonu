def solve(start, end):
    if end - start < 2:
        # print(start, end)
        if data[start] < data[end]:
            if data[start] == 1 and data[end] == 3:
                return start
            return end
        elif data[start] > data[end]:
            if data[start] == 3 and data[end] == 1:
                return end
            return start
        else:
            return start

    # start부터 end까지의 학생들의 승자를 구하기 위해서
    # 절반 start ~ (start+end) // 2
    m = (start + end) // 2
    w1 = solve(start, m)
    w2 = solve(m + 1, end)
    return solve(solve(start, m), solve(m + 1, end))

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    data = list(map(int, input().split()))

    print(f'#{tc} {solve(0, N - 1) + 1}')