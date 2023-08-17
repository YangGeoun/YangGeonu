
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int,input().split()))
    hoaduck = [i+1 for i in range(N)]          # 화덕에 몇번 피자가 들어 있는지 확인하기위한 리스트
    pizza_num = N + 1                          # 다음에 넣을 피자의 번호
    q = []                                      # 피자를 화덕에서 돌릴 큐
    count = -1                                  # 피자를 1번 회전한 횟수(1번 피자 -> 2번 피자 이동하면 1번)
    for i in range(N):                          # 큐에 화덕 가득 피자를 넣는다.
        q.append(arr.pop(0))

    while len(q) != 1:                           # 큐에 1개의 요소가 남을때까지 반복
        temp = q.pop(0)                          # 1번 피자를 꺼낸다.
        count = (count + 1) % len(hoaduck)       # 1번 돌려줄때마다 count +1
        temp = temp // 2                         # 꺼낸 피자 치즈량 절반으로 만든다.
        if temp != 0:                            # 치즈가 0이 안 되면
            q.append(temp)                       # 다시 화덕에 넣는다.
        else:                                    # 치즈량이 0이 되면
            if arr:                              # 아직 피자가 남았으면
                b = arr.pop(0)                   # 그 피자를 리스트에서 꺼내서
                q.append(b)                      # 화덕에 넣는다.
                hoaduck.pop(count)                # 나중에 확인 하기 위한 화덕에서도 피자를 꺼낸다.
                hoaduck.insert(count, pizza_num)  # 나중에 확인 하기 위한 화덕에도 새 피자를 넣어준다.
                pizza_num += 1                    # 피자 번호를 1 올려준다.
            else:                                 # 더 넣을 피자가 없으면
                hoaduck.pop(count)                # 확인을 위한 화덕에서 0이 된 피자를 빼준다.
                count -= 1                        #
    print(f'#{tc} {hoaduck[0]}')



