def Power(b, e):
    global cnt
    cnt += 1
    if e == 0 or b == 0:
        return 1
    if e % 2 ==0:
        nb = Power(b, e/2)
        return nb * nb
    else:
        nb = Power(b,(e-1)/2)
        return (nb*nb) * b

cnt = 0
print(Power(2,1024))
print(cnt)