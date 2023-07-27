lst = [8,7,5,1,6,3,2,4,9,0]
print(lst)
for j in range(len(lst)-1):
    for i in range(len(lst)-1-j): #첫번째요소와 두번째요소, 두번째요소와 세번째요소를 계속비교해간다.
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1] , lst[i]
            print(lst)

print(lst)