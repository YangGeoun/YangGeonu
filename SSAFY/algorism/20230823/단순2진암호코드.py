dic = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
       '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9 }
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]
    si, sj = 0,0
    for i in range(N):
        for j in range(M-1,-1,-1):
            if arr[i][j] == 1:
                si, sj = i, j - 55
                break

    result = []
    for i in range(0, 56, 7):
        ans = ''
        for j in range(7):
            ans += str(arr[si][sj+i+j])
        result.append(dic[ans])

    if ((result[0] + result[2] + result[4] + result[6]) * 3 + result[1] + result[3] + result[5] + result[7]) % 10 == 0:
        sum = 0
        for el in result:
            sum += el
        print(f'#{tc} {sum}')
    else:
        print(f'#{tc} 0')
