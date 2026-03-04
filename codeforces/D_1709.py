t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    
    ans = []
    for i in range(n):
        for j in range(n-1):
            if a[j] > a[j + 1]:
                a[j],a[j + 1] = a[j + 1],a[j] 
                ans.append([1,j+1])
            if b[j] > b[j+1]:
                b[j],b[j + 1] = b[j + 1],b[j]
                ans.append([2,j+1])
    for i in range(n):
        if a[i] > b[i]:
            b[i],a[i] = a[i],b[i] 
            ans.append([3,i+1])
    print(len(ans))
    for v in ans:
        print(v[0],v[1])