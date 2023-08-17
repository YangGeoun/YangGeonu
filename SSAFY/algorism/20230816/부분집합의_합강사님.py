def solve(idx,sum_v):
    global cnt
    if sum_v == target:
        print(t_lst)
        return sum_v
    elif sum_v > target:
        return sum_v
    if idx == N:
        return sum_v
    else:
        for j in range(N):
            if selected[j] == 0:
                selected[j] = 1
                t_lst[j] = arr[j]
                solve(idx+1,sum_v + arr[j])
                t_lst[j] = 0
                selected[j] = 0



cnt = 0
N = 10
arr = [i+1 for i in range(N)]
selected = [0] * N
target = 10
t_lst = [0] * N
solve(0,0)
print(cnt)