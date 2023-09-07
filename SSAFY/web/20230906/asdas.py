S = input()
ans = 0

for index in range(len(S)):
    if 64 < ord(S[index]) < 83:
        ans += ((ord(S[index])-65)//3) + 3
    elif ord(S[index]) == 83:
        ans += 8
    elif 83 < ord(S[index]) < 87:
        ans += 9
    else:
        ans += 10
print(ans)