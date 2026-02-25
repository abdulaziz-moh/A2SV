t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    
    
    ans = [a[0]]
    dxn = 1
    if a[1] < a[0]:
        dxn = -1
    i = 1
    
    while i < n:
        if dxn == 1:
            while i < n and a[i] > a[i-1]:
                i += 1
            ans.append(a[i-1])
            dxn = -1
        else:
            while i < n and a[i] < a[i-1]:
                i += 1
            ans.append(a[i-1])
            dxn = 1
    print(len(ans))
    for v in ans:
        print(v, end=" ")
    print()