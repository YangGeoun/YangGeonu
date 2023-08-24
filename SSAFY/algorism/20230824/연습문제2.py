
# M = ['0', 'F', '9', '7', 'A', '3']
M = list('01D06079861D79F99F')
ans = ''
for el in M:
    if el.isdigit():
        ten_num = int(el)
    else:
        ten_num = ord(el) - 55
    tmp = ''
    while ten_num:
        tmp = str(ten_num % 2) + tmp
        ten_num //= 2
    while len(tmp) != 4:
        tmp = '0' + tmp
    ans += tmp
for i in range(0,len(ans),7):
    temp = ''
    for j in range(7):
        if i+j == len(ans):
            break
        temp += ans[i+j]
    result = 0
    k = 0
    for j in range(len(temp)-1,-1,-1):
        if temp[j] == '1':
            result += 2 ** k
        k += 1
    print(result, end=' ')

