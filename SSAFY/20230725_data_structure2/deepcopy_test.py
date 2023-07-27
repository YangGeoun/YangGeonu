

# 할당
a = [1,2,3]
b = a
b[0] = 100
print(a , b)

# 슬라이싱 (얕은 복사)
a = [1,2,3]
b = a[:]
b[0] = 100
print(a , b)

# copy (얕은 복사)
c = a.copy()
c[0] = 100
print(a, c)

# 얕은 복사의 한계
a = [1, 2, [3, 4]]
b = a[:]
b[2][0] = 100
print(a, b)

a = [1, 2, [3, 4]]
c = a.copy()
c[2][0] = 99
print(a, c)

# 깊은 복사
import copy
a = [1, 2, [3, 4]]
c = copy.deepcopy(a)
c[2][0] = 99
print(a, c)

#복사의 과정이 이미지화되지 않으면 파이썬 튜터 돌려보기