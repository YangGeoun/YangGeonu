x = int(input())
y = int(input())
q = 0

if x > 0 and y > 0:
    q = 1
elif x > 0 and y < 0:
    q = 4
elif x < 0 and y < 0:
    q = 3
elif x < 0 and y > 0:
    q = 2

print(q)