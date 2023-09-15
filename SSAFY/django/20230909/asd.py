import math

a = [0,0]
b = [-1,-1]

# 거리구하기
distance = math.sqrt(((b[0] - a[0])**2) + ((b[1] - a[1])**2))

# 각도 구하기
angle_radian = math.atan((b[1] - a[1])/(b[0] - a[0]))
angle_gak = 180 * angle_radian / math.pi
if (b[1] - a[1]) < 0 and (b[0] - a[0]) > 0:
    angle_gak = 90 - angle_gak

if (b[1] - a[1]) > 0 and (b[0] - a[0]) < 0:
    angle_gak = 90 - angle_gak
angle2 = (b[1] - a[1])/(b[0] - a[0])

print(angle_gak)