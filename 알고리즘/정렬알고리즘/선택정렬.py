# 가장 작을 요소를 찾고 그 요소를 가장 앞에 놓는다.
list = [5,4,6,7,8,3,2,0,9,1]
N = len(list)
for i in range(0,N):
    min_index = N-1
    for j in range(i,N-1):
        if list[min_index] > list[j]:
            min_index = j
        temp = list[min_index]
    list[i], list[min_index] = list[min_index], list[i]  #튜플로 만들어서 언팩킹
print(list)

