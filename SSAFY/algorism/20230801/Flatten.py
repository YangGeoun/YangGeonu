T = 10
for tc in range(1, T+1):
    N = int(input())
    box_list = list(map(int, input().split()))
    high_list = [0] * 102
    for el in box_list:
        high_list[el] += 1
    i = 101
    j = 1
    for dump in range(N):
        while True:
            if high_list[i] != 0:
                high_list[i] -= 1
                high_list[i-1] += 1
                if high_list[i] == 0:
                    i -= 1
                break
            else:
                i -= 1
        while True:
            if high_list[j] != 0:
                high_list[j] -= 1
                high_list[j+1] += 1
                if high_list[j] == 0:
                    j += 1
                break
            else:
                j += 1
    print(f'#{tc} {i - j}')

