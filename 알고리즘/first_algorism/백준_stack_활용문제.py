T = int(input()) #실행 횟수
list = []
i = 0
sum = 0

while i < T:
    a = int(input())
    if(a == 0):
        del list[-1]
    else:
        list.append(a)
    i += 1
for num in list:
    sum += num

print(sum)

    