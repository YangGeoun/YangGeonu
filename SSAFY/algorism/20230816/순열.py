def f(i,N):
    if i == N:
        print(a)
    else:
        for j in range(i,N):
            a[i], a[j] = a[j], a[i]
            f(i+1,N)
            a[i], a[j] = a[j], a[i]


def f2(i,N):
    if i == N:
        print(a)
    else:
        for j in range(i,N):
            a[i], a[j] = a[j], a[i]
            f2(i+1,N)


# perm_arr[idx]에 들어갈 수 있는 애들 다 넣어보기
# 중복순열
def perm(idx):
    if idx == N:
        print(perm_arr)
        return
    for i in range(N):
        perm_arr[idx] = a[i]
        perm(idx+1)


# 그냥 순열(중복x)
def perm1(idx):
    if idx == N:
        print(perm_arr)
        return
    for i in range(N):
        if selected[i] == 0:       # 안 쓴 애만 쓸거다
            perm_arr[idx] = a[i]
            selected[i] = 1        # 썼으면 표시하기
            perm1(idx+1)
            selected[i] = 0        # 다음 경우의 수 넘어 깔때 썼다는 표시 지우기


N = 3
a = [i+1 for i in range(N)]
arr = [i+1 for i in range(N)]
perm_arr = [0] * N
selected = [0] * N
f(0,N)
f2(0,N)
