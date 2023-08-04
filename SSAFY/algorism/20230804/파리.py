T = int(input())
for tc in range(1, T + 1):
    l, a, b, f = map(int, input().split())
    t = l / (a+b)
    d = f * t
    print(d)