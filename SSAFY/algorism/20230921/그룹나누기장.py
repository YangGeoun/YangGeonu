# x,y 노드를 하나의 집합으로 만들어주기
# x가 포함된 집합과 ,y가 포함된 집합을 하나의 집합으로 만들기
def union(x,y):
    xr = find_set(x)
    yr = find_set(y)
    # 한쪽 대표자의 부모를 다른쪽 집합의 대표로 만들어 주면 됩니다.
    arr[xr] = yr  # 반대도 상관없음


# x가 포함된 집합의대표자를 반환하는 함수
# 왜반환???? x가 어떤 집합에 포함되었는지 확인하는 함수
def find_set(x):
    # 대표자는 노드번호와 부모노드번호가 일치하는 노드
    if x == arr[x] :
        return x
    # 스스로가 대표자가 아니면....몰라/...부모에게 물어보기
    arr[x] = find_set(arr[x])
    return arr[x]


T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())  # N명이 있고 M 장의신청서
    arr = [a for a in range(N+1)]
    sin = list(map(int,input().split()))
    for i in range(0,len(sin),2):
        union(sin[i],sin[i+1])

    aset = set()
    for i in range(1,len(arr)):
        aset.add(find_set(i))
    print(len(aset))