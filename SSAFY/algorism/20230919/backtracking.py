
def subset(cnt, sum_v):
    if sum_v > 10:
        return
    if cnt == 10:
        if sum_v == 10:
            print(path)
        return
    path[cnt] = arr[cnt]
    subset(cnt+1, sum_v + arr[cnt])
    path[cnt] = 0
    subset(cnt+1, sum_v)


arr = [i for i in range(1, 11)]
path = [0] * 10
subset(0,0)