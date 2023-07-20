matrix_in = []
max_num = 0
max_idx_x = 1
max_idx_y = 1
# max_idx_x 와 max_idx_y 의 초기값을 모두 0으로 설정하면 
# 모든 입력이 0 일때 0행, 0렬 을 출력하여 문제를 틀리게 된다.

for i in range(9):
    temp = list(map(int, input().split()))
    matrix_in.append(temp)

for i in range(9):
    for j in range(9):
        if matrix_in[i][j] > max_num:
            max_num = matrix_in[i][j]
            max_idx_x = i + 1
            max_idx_y = j + 1

print(max_num)
print(max_idx_x, max_idx_y)