for tc in range(10):
    N = int(input())
    apt_list = list(map(int, input().split()))
    jm = 0
    j = 2
    while j < len(apt_list) - 2:
        max_high = 0
        for i in range(5):
            if i == 2:
                continue
            if apt_list[j - 2 + i] > max_high:
                max_high = apt_list[j - 2 + i]
        if apt_list[j] > max_high:
            jm += apt_list[j] - max_high
        j + = 1

    print(f'#{tc + 1} {jm}')



3
7 4 2 0 0 6 0 7 0 3
3 4 2 9 0 0 3 8 2 4
3 2 5 6 4 7 0 4 9 9


7
6
2