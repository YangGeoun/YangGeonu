
def comb(i,cnt):
    if cnt == 7:
        # print(selected)
        sum_v = 0
        for j in range(9):
            if selected[j] == 1:
                sum_v += lst[j]
        # print(sum_v)
        for j in range(9):
            if sum_v == 100:
                lst.sort()
                print(lst[j])
        return

    if i == 9:
        return

    selected[i] = 1
    comb(i+1,cnt+1)
    selected[i] = 0
    comb(i+1,cnt)



lst = []

for _ in range(9):
    tall = int(input())
    lst.append(tall)
# print(lst)   아홉명 난쟁이들키
# 9명중 7명 뽑아서 합이 100이 되는 키들 출력
selected = [0] * 9
comb(0,0)


#정렬 중복