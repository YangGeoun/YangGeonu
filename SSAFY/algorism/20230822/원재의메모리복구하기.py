# 0으로 시작해서 앞에서부터 하나씩 보면서 0에서 1로 다시 1에서 0으로
# 총 몇번 바뀌었는지가 총 메모리를 고치는 횟수와 같다.
# 그래서 state라는 변수를 만등러 현재 보고있는 숫자가 무엇인지 담고
# 값이 바뀌는 시점에 cnt를 올려주었다.


T = int(input())
for tc in range(1,1+T):
    lst = list(map(int, input()))
    cnt = 0
    state = 0
    for el in lst:
        if el != state:
            cnt += 1
            state = el
    print(f'#{tc} {cnt}')
