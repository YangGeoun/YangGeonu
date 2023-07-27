T = 20
hag_sum = 0
pyung_sum = 0

for i in range(20):
    name, hag, pyung = input().split()
    hag_sum += float(hag)
    if pyung == 'A+':
        pyung_sum += 4.5 * float(hag)
    elif pyung == 'A0':
        pyung_sum += 4 * float(hag)
    elif pyung == 'B+':
        pyung_sum += 3.5 * float(hag)
    elif pyung == 'B0':
        pyung_sum += 3 * float(hag)
    elif pyung == 'C+':
        pyung_sum += 2.5 * float(hag)
    elif pyung == 'C0':
        pyung_sum += 2 * float(hag)
    elif pyung == 'D+':
        pyung_sum += 1.5 * float(hag)
    elif pyung == 'D0':
        pyung_sum += 1 * float(hag)
    elif pyung == 'F':
        pyung_sum += 0
    elif pyung == 'P':
        hag_sum -= float(hag)


print(pyung_sum / hag_sum)