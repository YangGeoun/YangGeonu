T = int(input())
for tc in range(1, T + 1):
    S = 13
    D = 13
    H = 13
    C = 13
    input_str = input()
    cards = []
    ans = 0
    for i in range(0, len(input_str), 3):
        temp = ''
        for j in range(3):
            temp += input_str[i+j]
        if temp in cards:
            ans = 1
            break
        else:
            cards.append(temp)
        if temp[0] == 'S':
            S -= 1
        elif temp[0] == 'D':
            D -= 1
        elif temp[0] == 'H':
            H -= 1
        elif temp[0] == 'C':
            C -= 1
    if ans:
        print(f'#{tc}','ERROR')
    else:
        print(f'#{tc}',S,D,H,C)