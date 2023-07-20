xy_list = []
x_list = [0] * 100
for i in range(100):
    xy_list.append(x_list[:])
sum = 0


def paper(x, y):
    global xy_list
    for i in range(10):
        for j in range(10):
            xy_list[x+i][y+j] = 1


T = int(input())
for tx in range(T):
    a, b = map(int, input().split())
    paper(a, b)

for i in range(100):
    for j in range(100):
        sum += xy_list[i][j]

print(sum)