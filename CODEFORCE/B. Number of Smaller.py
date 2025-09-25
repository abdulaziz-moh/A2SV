n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

l, r = 0, 0
while l < n and r < m:
    while l < n and a[l] < b[r]:
        l += 1
    print(l,end=" ")
    r += 1
while r < m:
    print(l,end=" ")
    r += 1