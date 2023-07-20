T = int(input())
answer = 0

for tc in range(T):
    arr = []
    add = 1
    S = input()
    for i in range(len(S)):
        try:
            if S[i] == S[i+1]:
                continue
        except:
            arr.append(S[i])
        else:
            arr.append(S[i])
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                continue
            elif arr[i] == arr[j]:
                add = 0
    answer += add

print(answer)



            