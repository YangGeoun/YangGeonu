def solve(idx):
    global min_v
    if idx > len_N - 2 and idx > 0:
        tmp_num = ''
        for i in range(idx):
            tmp_num += str(tmp[i])
        sub = abs(num - int(tmp_num))
        if min_v > sub + idx:
            min_v = sub + idx
        if idx == len_N + 1:
            return
    for el in lst:
        tmp[idx] = el
        solve(idx + 1)


N = input()
num = int(N)
len_N = len(N)
M = int(input())
temp_lst = []
if M != 0:
    temp_lst = list(map(int, input().split()))
    temp_lst.sort(reverse=True)
lst = [0,1,2,3,4,5,6,7,8,9]
for el in temp_lst:
    lst.pop(el)
tmp = [0] * (len_N + 1)
min_v = 500001
solve(0)
if num == 100:
    print(0)
elif min_v == 500001:
    print(abs(num-100))
elif abs(num-100) < min_v:
    print(num-100)
else:
    print(min_v)

