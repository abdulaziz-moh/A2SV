n = int(input())
a = []
for _ in range(n):
    x = list(map(int,input().split()))
    a.append(x)
    
comp = max(a[0][0],a[0][1])
for i in range(1,n):
    if a[i][1] > comp:
        if a[i][0] > comp:
            print('NO')
            break
        else:
            comp = a[i][0]
    elif a[i][0] <= comp:
        comp = max(a[i][0],a[i][1])
    else:
        comp = a[i][1]
    
else:
    print('YES')