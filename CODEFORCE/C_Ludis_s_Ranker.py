n = int(input())
ab = list(map(int,input().split()))
a= sorted(ab,reverse=True)

i = 1
rank = 2
hm = {}
hm[a[0]] = '1'

while i < n:
    while i < n and a[i] == a[i-1]:
        hm[a[i]] = hm[a[i-1]]
        rank += 1
        i += 1
    if i < n:
        hm[a[i]] = str(rank)
        rank += 1
        i += 1
for v in ab:
    print(hm[v], end=" ")
