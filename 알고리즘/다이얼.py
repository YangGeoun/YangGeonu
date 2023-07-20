# a, b, c = 3
# d, e, f = 4
# g, h, i = 5
# j, k, l = 6
# m, n ,o = 7
# p,q,r,s = 8
# t, u, v = 9
# w, x, y, z = 10

S = input()
arr = []

for index in range(len(S)):
    if 64 < ord(S[index]) < 83:
        arr.append(((ord(S[index])-65)//3) + 3)
    elif ord(S[index]) == 83:
        arr.append(8)
    elif 83 < ord(S[index]) < 87:
        arr.append(9)
    else:
        arr.append(10)

sum = 0

for i in arr:
    sum += i

print(sum)