# 각 제목을 리스트에 담아놓을 것이다.
# 리스트에 담겨있는 제목 모두 검사해서 제목의 첫글자가
# A가 있는지부터 시작해서 Z가 있는지까지 검사할 것이다.
# if lst[i][0] == 'A': 형식으로 만들면 A~Z까지 전부 만들어야하므로
# 아스키코드로 변환하여 ord(lst[i][0]) == 65: 으로 하여 1씩 증가시키며 검사할 것이다.
# 그러나 하나라도 비면(ex: C가 없으면) 반복문을 바로 끊어버릴 것이다.

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = [input() for _ in range(N)]
    Alphabet = ord('A')
    while Alphabet != ord('Z') + 1:
        is_Alphabet = False
        for el in lst:
            if ord(el[0]) == Alphabet:
                is_Alphabet = True
        if is_Alphabet:
            Alphabet += 1
        else:
            break
    print(f'#{tc} {Alphabet - ord("A")}')
