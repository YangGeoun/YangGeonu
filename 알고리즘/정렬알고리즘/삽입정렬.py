lst = [8,7,5,1,6,3,2,4,9,0]

#요소를 뽑아내어 이를 적당한 곳에 삽입
# print(lst)
for i in range(len(lst)):
    if i == 0:
        continue                  
    for j in range(i):                  # i번째 0~(i-1)까지의 요소와 비교해서 적당한 자리에 넣는다. 
        temp = lst[i]                   # lst i 번째 요소를 temp에 담는다.
        if lst[j] > temp:               # i번째 이전요소는 정렬되 있을 것이다. 그러므로 앞에서부터 비교하면서 temp가 비교한 요소보다 작아질때 그 요소 앞에 들어가면 된다.
            for k in range(i-j):        # 비교한 요소 앞에 들어가기 위해서 비교한 요소부터 (i-1)번째 요소의 자리를 1씩 밀어주어야한다.
                lst[i-k] = lst[i-k-1]
                # print(lst)
                # print(temp)
            lst[j] = temp
            # print(lst)
            # print(temp)

print(lst)