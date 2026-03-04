from collections import defaultdict

n, k, q = map(int,input().split())
ltrt, query = [], []
mx = 200000
for _ in range(n):
    ltrt.append(list(map(int,input().split())))
    a,b = ltrt[-1]

for _ in range(q):
    query.append(map(int,input().split()))
count = [0]*(mx+2)
for l,r in ltrt:
    count[l] += 1
    count[r+1] -= 1
for i in range(1,len(count)):
    count[i] += count[i-1]

accumlator = 0
for i in range(len(count)):
    if count[i] >= k:
        accumlator += 1
    count[i] = accumlator
for l,r in query:
    if l > 0:
        print(count[r] - count[l-1])
    else:
        print(count[r])