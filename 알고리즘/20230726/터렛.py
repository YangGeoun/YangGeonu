import sys
import math

T = int(sys.stdin.readline())

for tc in range(T):
    A = map(int, sys.stdin.readline().split())
    x1,y1,r1,x2,y2,r2 = A
    
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    if r1 >= r2:
        max_r = r1
        min_r = r2
    else:
        max_r = r2
        min_r = r1

    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif distance < max_r:
        if min_r + distance > max_r:
            print(2)
        elif min_r + distance == max_r:
            print(1)
        else:
            print(0)
    elif  distance < max_r:
        if min_r == 0:
            print(1)
        else:
            print(2)
    else:
        if distance == (r1 + r2):
            print(1)
        elif distance < (r1 + r2):
            print(2)
        else:
            print(0)
