t = int(input())
for j in range(t):
    n,m = list(map(int,input().split()))
    val = []
    for i in range(n):
        val.append(input())
    sum,count,i = 0,0,0

    while (i<n and sum<m):
        sum += len(val[i])
        if sum <= m:
            count += 1
            i += 1
        else:
            break
    print(count)
