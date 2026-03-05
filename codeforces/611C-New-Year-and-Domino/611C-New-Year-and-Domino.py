h, w = map(int, input().split())
s,queries = [], []
for _ in range(h):
    s.append(input())
for _ in range(int(input())):
    queries.append(map(int,input().split()))
prefixrow, prefixcol = [], []

for v in s:
    status = True
    arr = [0]
    for i in range(w):
        if v[i] == '.':
            if status:
                arr.append(arr[-1])
                status = False
            else:
                arr.append(arr[-1] + 1)
        else:
            status = True
            arr.append(arr[-1])
    prefixrow.append(arr)
for i in range(w):
    status = True
    arr = [0]
    for j in range(h):
        if s[j][i] == '.':
            if status:
                arr.append(arr[-1])
                status = False
            else:
                arr.append(arr[-1] + 1)
        else:
            status = True
            arr.append(arr[-1])
    prefixcol.append(arr)

for r1,c1,r2,c2 in queries:
    sum = 0
    for i in range(r1-1,r2):
        sum += (prefixrow[i][c2] - prefixrow[i][c1])
    for i in range(c1-1,c2):
        sum += (prefixcol[i][r2] - prefixcol[i][r1])
    print(sum)