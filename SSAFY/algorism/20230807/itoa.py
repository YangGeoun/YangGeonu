a = 123
ans = ''
while a > 0:
    b = a % 10
    a = a // 10
    c = chr(ord('0')+b)
    ans = c + ans
print(ans)
print(type(ans))