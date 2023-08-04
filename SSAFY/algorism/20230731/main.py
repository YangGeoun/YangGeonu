T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input()))
    temp_list = [0] * 10
    for el in num_list:
        temp_list[el] += 1
    max_n = 0
    max_i = 0
    for i in range(len(temp_list)):
        if max_n <= temp_list[i]:
            max_n = temp_list[i]
            max_i = i
    print(f'#{tc} {max_i} {max_n}')