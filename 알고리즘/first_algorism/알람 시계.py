h, m = map(int, input().split())

if m < 45:
    h = h -1 
    m = m + 15
else:
    m = m - 45

if h == -1:
    h = 23

print(f'{h} {m}')
