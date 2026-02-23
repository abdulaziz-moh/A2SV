n,m = map(int,input().split())
a = []
sum = 0
for _ in range(n):
    x = list(map(int,input().split()))
    x.append(x[0]-x[1])
    sum += x[0]
    a.append(x)
    
a.sort(reverse=True, key = lambda x:x[2])
count, i = 0,0
while i < n and sum > m:
    sum -= a[i][2]
    count += 1
    i += 1
if sum > m:
    print(-1)
else:
    print(count)