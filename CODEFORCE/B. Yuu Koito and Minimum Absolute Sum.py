t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    
    if a[0] == -1 and a[n-1] == -1:
        a[0],a[n-1] = 0,0
    elif a[0] == -1:
        a[0] = a[n-1]
    elif a[n-1] == -1:
        a[n-1] = a[0]
            
    for i in range(1,n-1):
        if a[i] == -1:
            a[i] = 0
    print(abs(a[n-1] - a[0]) )
    print(*a)