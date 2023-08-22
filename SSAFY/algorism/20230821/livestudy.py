def preorder(n):
    if n:   # 존재하는 정점이면
        print(n, end = ' ')
        preorder(ch1[n])          # 왼쪽 서브트리로 이동
        preorder(ch2[n])


def inorder(n):
    if n:   # 존재하는 정점이면
        inorder(ch1[n])
        print(n, end = ' ')
        inorder(ch2[n])


def postorder(n):
    if n:   # 존재하는 정점이면
        postorder(ch1[n])
        postorder(ch2[n])
        print(n, end = ' ')



V = int(input())
arr = list(map(int, input().split()))
ch1 = [0] * (V+1)
ch2 = [0] * (V+1)
par = [0] * (V+1)
for i in range(V-1):
    if ch1[arr[i*2]] == 0:
        ch1[arr[i*2]] = arr[i*2+1]
    else:
        ch2[arr[i*2]] = arr[i*2+1]
    par[arr[i*2+1]] = arr[i*2]
#
preorder(1)
print()
inorder(1)
print()
postorder(1)

# root = 1
# while par[root] != 0:
#     root += 1
# print(root)
