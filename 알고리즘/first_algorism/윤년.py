q = int(input())
a = 0

if (q % 4 == 0 and q % 100 != 0) or q % 400 == 0:
    a = 1
else:
    a = 0

print(a)