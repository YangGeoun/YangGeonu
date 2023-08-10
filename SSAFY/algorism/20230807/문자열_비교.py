T = int(input())
for tc in range(1, 1+T):
    check_str = input()
    full_str = input()
    ans = 0
    for i in range(len(full_str)-len(check_str) + 1):
        check = 1
        for j in range(len(check_str)):
            if full_str[i+j] != check_str[j]:
                check = 0
        if check == 1:
            ans = 1
    print(f'#{tc} {ans}')