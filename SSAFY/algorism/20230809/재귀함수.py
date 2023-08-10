memo = {0:0, 1:1, 2:1}
memol = [0] * 101
memol[1] = 1

def pibodic(num):
    global memo
    if num in memo:
        return memo[num]
    memo[num] = pibodic(num - 1) + pibodic(num - 2)
    return memo[num]


def pibolst(num):
    global memol
    if num >= 2 and memol[num] == 0:
        memol[num] = (pibolst(num-1) + pibolst(num-2))
    return memol[num]


for i in range(100):
    print(pibodic(i))

for i in range(100):
    print(pibolst(i))