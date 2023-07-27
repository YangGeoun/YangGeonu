s = input()
S = s.upper()
S_list = [0] * 26

for i in S:
    S_list[ord(i)-65] += 1

max_i_1 = 0
max_i_2 = 0
max_num = 0

for i in range(len(S_list)):
    if S_list[i] > max_num:
        max_num = S_list[i] 
        max_i_1 = i

max_num = 0
for i in range(len(S_list)):
    if S_list[len(S_list)-i-1] > max_num:
        max_num = S_list[len(S_list)-i-1]
        max_i_2 = len(S_list)-i-1

if max_i_1 == max_i_2:
    print(chr(max_i_1+65))
else:
    print('?')