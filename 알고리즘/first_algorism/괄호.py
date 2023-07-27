T = int(input())

i = 0
count = 0

while i < T:
    list = input()
    for x in list:
        if x == '(':
            count += 1
        elif x == ')':
            count += -1
        if count < 0:
            break
    if count == 0:
        print('YES')
    else:
        print('NO')
    count = 0
    i +=1
