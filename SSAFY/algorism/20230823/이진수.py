T = int(input())
for tc in range(1,T+1):
    N, M = input().split()
    ans = ''
    for el in M:
        if el.isdigit():
            ten_num = int(el)
        else:
            ten_num = ord(el) - 55
        tmp = ''
        while ten_num:
            tmp = str(ten_num % 2) + tmp
            ten_num //= 2
        while len(tmp) != 4:
            tmp = '0' + tmp
        ans += tmp
    print(f'#{tc} {ans}')